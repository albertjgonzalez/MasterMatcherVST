import os
import sys
import json
import matchering as mg
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

def process_audio(user_track_path: str, reference_track_path: str, output_path: str) -> dict:
    """
    Process audio using Matchering
    
    Args:
        user_track_path: Path to the user's track
        reference_track_path: Path to the reference track
        output_path: Path where the processed track should be saved
        
    Returns:
        Dictionary with processing results and metadata
    """
    try:
        logger.info("Starting audio processing...")
        
        # Validate input files
        if not os.path.exists(user_track_path):
            raise FileNotFoundError(f"User track not found: {user_track_path}")
            
        if not os.path.exists(reference_track_path):
            raise FileNotFoundError(f"Reference track not found: {reference_track_path}")
            
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_path)
        os.makedirs(output_dir, exist_ok=True)
        
        # Process audio using Matchering
        # Note: In newer versions of Matchering, we don't need to call init()
        # Note: The API has changed in newer versions
        mg.process(
            target=user_track_path,
            reference=reference_track_path,
            results=[
                mg.pcm24(output_path)
            ]
        )
        
        # Log success manually since we removed the log parameter
        logger.info("Processing complete!")
        
        logger.info("Processing complete!")
        return {
            "status": "success",
            "output_path": output_path,
            "message": "Processing completed successfully"
        }
        
    except Exception as e:
        logger.error(f"Error processing audio: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }

def main():
    """
    Main entry point when running as a script
    """
    if len(sys.argv) != 4:
        print("Usage: python processor.py <user_track> <reference_track> <output_path>")
        sys.exit(1)
        
    user_track = sys.argv[1]
    reference_track = sys.argv[2]
    output_path = sys.argv[3]
    
    result = process_audio(user_track, reference_track, output_path)
    print(json.dumps(result))

if __name__ == "__main__":
    main()
