import json
import subprocess
import os
from pathlib import Path
import logging
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

def process_tracks(user_track_path: str, reference_track_path: str) -> dict:
    """
    Process tracks using the processor script
    
    Args:
        user_track_path: Path to the user's track
        reference_track_path: Path to the reference track
        
    Returns:
        Dictionary with processing results
    """
    try:
        # Create output directory
        output_dir = Path(os.getenv('OUTPUT_DIR', 'processed'))
        output_dir.mkdir(exist_ok=True)
        
        # Generate output filename
        output_filename = f"processed_{Path(user_track_path).stem}.wav"
        output_path = str(output_dir / output_filename)
        
        logger.info(f"Processing tracks: {user_track_path} -> {output_path}")
        
        # Run the processor script
        result = subprocess.run(
            [
                "python",
                "processor.py",
                user_track_path,
                reference_track_path,
                output_path
            ],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            logger.error(f"Processor error: {result.stderr}")
            return {
                "status": "error",
                "message": f"Processor failed: {result.stderr}"
            }
            
        # Parse the JSON output
        try:
            output = json.loads(result.stdout)
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON output: {result.stdout}")
            return {
                "status": "error",
                "message": "Invalid JSON output from processor"
            }
            
        return output
        
    except Exception as e:
        logger.error(f"Error processing tracks: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }

def main():
    """
    Main entry point for the server
    """
    logger.info("Starting MasterMatcher server...")
    
    while True:
        # Wait for input from the C++ plugin
        try:
            input_data = input()
            if not input_data:
                continue
                
            # Parse the input
            try:
                data = json.loads(input_data)
                user_track = data['user_track']
                reference_track = data['reference_track']
            except (json.JSONDecodeError, KeyError) as e:
                logger.error(f"Invalid input data: {str(e)}")
                print(json.dumps({
                    "status": "error",
                    "message": f"Invalid input data: {str(e)}"
                }))
                continue
                
            # Process the tracks
            result = process_tracks(user_track, reference_track)
            
            # Send the result back to the C++ plugin
            print(json.dumps(result))
            sys.stdout.flush()
            
        except KeyboardInterrupt:
            logger.info("Server shutting down...")
            break
        except Exception as e:
            logger.error(f"Server error: {str(e)}")
            print(json.dumps({
                "status": "error",
                "message": f"Server error: {str(e)}"
            }))
            continue

if __name__ == "__main__":
    main()
