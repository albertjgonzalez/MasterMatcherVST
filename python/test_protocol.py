import subprocess
import json
import time
import sys
sys.path.append('src')

from protocol import (
    create_process_request,
    create_process_response,
    create_status_update,
    MessageType
)

def test_protocol():
    """Test the communication protocol"""
    print("\n=== Protocol Test ===")
    
    # Start the server in a subprocess
    print("\nStarting server...")
    server = subprocess.Popen(
        ["python", "src/server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )
    
    # Give server time to start
    time.sleep(1)
    
    try:
        # Test ping/pong
        print("\nTesting ping/pong...")
        ping_msg = {
            "type": MessageType.PING.value,
            "payload": {}
        }
        server.stdin.write(json.dumps(ping_msg) + "\n")
        server.stdin.flush()
        
        # Read response
        response = server.stdout.readline()
        print("Pong response:", response)
        
        # Test process request
        print("\nTesting process request...")
        request_msg = create_process_request(
            user_track="test_user.wav",
            reference_track="test_reference.wav",
            output_path="processed/test_output.wav"
        )
        
        server.stdin.write(request_msg + "\n")
        server.stdin.flush()
        
        # Read response
        response = server.stdout.readline()
        print("Process response:", response)
        
        # Test invalid message
        print("\nTesting invalid message...")
        invalid_msg = {
            "type": "invalid_type",
            "payload": {}
        }
        server.stdin.write(json.dumps(invalid_msg) + "\n")
        server.stdin.flush()
        
        # Read response
        response = server.stdout.readline()
        print("Error response:", response)
        
    finally:
        # Clean up
        print("\nShutting down server...")
        server.terminate()
        server.wait()

if __name__ == "__main__":
    test_protocol()
