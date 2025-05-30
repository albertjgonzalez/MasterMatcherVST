import os
import sys
import matchering as mg
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("\n=== Python Environment Test ===")
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")
print(f"Matchering version: {mg.__version__}")

# Test Matchering initialization
try:
    print("\nTesting Matchering initialization...")
    mg.init()
    print("Matchering initialized successfully!")
except Exception as e:
    print(f"Error initializing Matchering: {str(e)}")

print("\nTest complete!")
