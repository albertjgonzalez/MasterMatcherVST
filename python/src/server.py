import sys
import json
import subprocess
import os
from pathlib import Path
import logging
from dotenv import load_dotenv
from protocol import (
    Message,
    MessageType,
    ProcessRequest,
    ProcessResponse,
    StatusUpdate,
    ProtocolError,
    validate_message
)
import time
import matchering as mg

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class Server:
    """Main server class for handling communication with C++ plugin"""
    
    def __init__(self):
        self.is_processing = False
        self.processing_start_time = None
        self.processing_time = 0.0

    def process_audio(self, request: ProcessRequest) -> ProcessResponse:
        """
        Process audio using Matchering
        
        Args:
            request: ProcessRequest object containing track paths and parameters
            
        Returns:
            ProcessResponse object with processing results
        """
        try:
            logger.info("Starting audio processing...")
            self.is_processing = True
            self.processing_start_time = time.time()
            
            # Validate input files
            if not os.path.exists(request.user_track):
                raise FileNotFoundError(f"User track not found: {request.user_track}")
                
            if not os.path.exists(request.reference_track):
                raise FileNotFoundError(f"Reference track not found: {request.reference_track}")
            
            # Create output directory if it doesn't exist
            output_dir = os.path.dirname(request.output_path)
            os.makedirs(output_dir, exist_ok=True)
            
            # Send status update
            self.send_status("processing", 0.0, "Starting processing...")
            
            # Process audio using Matchering
            mg.process(
                target=request.user_track,
                reference=request.reference_track,
                results=[
                    mg.pcm24(request.output_path)
                ]
            )
            
            self.processing_time = time.time() - self.processing_start_time
            self.is_processing = False
            
            return ProcessResponse(
                status="success",
                output_path=request.output_path,
                message="Processing completed successfully",
                processing_time=self.processing_time
            )
            
        except Exception as e:
            logger.error(f"Error processing audio: {str(e)}")
            self.is_processing = False
            return ProcessResponse(
                status="error",
                message=str(e)
            )

    def send_status(self, status: str, progress: float, message: str):
        """Send status update to C++ plugin"""
        update = StatusUpdate(status, progress, message)
        print(update.to_message().to_json())
        sys.stdout.flush()

    def handle_message(self, message: Message):
        """Handle incoming message from C++ plugin"""
        try:
            validate_message(message)
            
            if message.type == MessageType.PROCESS_REQUEST:
                request = ProcessRequest(**message.payload)
                response = self.process_audio(request)
                print(response.to_message().to_json())
                sys.stdout.flush()
                
            elif message.type == MessageType.PING:
                response = Message(
                    type=MessageType.PONG,
                    payload={"status": "alive"}
                )
                print(response.to_json())
                sys.stdout.flush()
                
            else:
                logger.warning(f"Unknown message type: {message.type}")
                
        except ProtocolError as e:
            logger.error(f"Protocol error: {str(e)}")
            error = Message(
                type=MessageType.ERROR,
                payload={"message": str(e)}
            )
            print(error.to_json())
            sys.stdout.flush()

    def run(self):
        """Run the server main loop"""
        logger.info("Starting MasterMatcher server...")
        
        while True:
            try:
                # Read message from C++ plugin
                input_data = sys.stdin.readline()
                if not input_data:
                    continue
                    
                # Handle the message
                message = Message.from_json(input_data)
                self.handle_message(message)
                
            except KeyboardInterrupt:
                logger.info("Server shutting down...")
                break
            except Exception as e:
                logger.error(f"Server error: {str(e)}")
                error = Message(
                    type=MessageType.ERROR,
                    payload={"message": str(e)}
                )
                print(error.to_json())
                sys.stdout.flush()
                continue

def main():
    """Main entry point"""
    server = Server()
    server.run()

if __name__ == "__main__":
    main()
