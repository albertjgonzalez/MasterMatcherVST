import os
import sys
import json
import tempfile
import shutil
from pathlib import Path

# Add src directory to Python path
sys.path.append(str(Path(__file__).parent / 'src'))

from processor import process_audio

def create_test_file(filename: str, duration_seconds: int = 5) -> str:
    """
    Create a test audio file with random noise
    """
    import numpy as np
    import soundfile as sf
    
    # Generate random audio data (5 seconds of random noise)
    sample_rate = 44100
    duration_samples = duration_seconds * sample_rate
    audio_data = np.random.randn(2, duration_samples).astype(np.float32)
    
    # Create temporary directory
    temp_dir = tempfile.mkdtemp()
    test_file = os.path.join(temp_dir, filename)
    
    # Save audio file
    sf.write(test_file, audio_data.T, sample_rate)
    
    return test_file, temp_dir

def test_audio_processing():
    """
    Test the audio processing functionality
    """
    try:
        print("\n=== Audio Processing Test ===")
        
        # Create test files
        print("Creating test audio files...")
        user_track, temp_dir = create_test_file("test_user.wav")
        reference_track = create_test_file("test_reference.wav")[0]
        
        # Process audio
        print("\nProcessing audio...")
        output_path = os.path.join(temp_dir, "processed.wav")
        result = process_audio(user_track, reference_track, output_path)
        
        # Print results
        print("\nProcessing result:")
        print(json.dumps(result, indent=2))
        
        # Verify output file exists
        if result["status"] == "success":
            assert os.path.exists(result["output_path"]), "Processed file not found"
            print("\nTest successful! Processed file created.")
        else:
            print(f"\nTest failed: {result['message']}")
            
    except Exception as e:
        print(f"\nTest failed with error: {str(e)}")
    finally:
        # Clean up
        print("\nCleaning up test files...")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

if __name__ == "__main__":
    test_audio_processing()
