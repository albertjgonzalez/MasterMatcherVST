# Python Environment Setup

This directory contains the Python backend for the MasterMatcher VST plugin.

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- macOS/Linux:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in this directory with the following variables:
```env
OUTPUT_DIR=processed  # Directory for processed audio files
```

## Running the Server

To start the Python server:
```bash
python server.py
```

The server will run continuously and listen for processing requests from the C++ plugin.

## Communication Protocol

The server communicates with the C++ plugin using JSON over stdin/stdout:

### Request Format
```json
{
    "user_track": "path/to/user/track.wav",
    "reference_track": "path/to/reference/track.wav"
}
```

### Response Format
```json
{
    "status": "success|error",
    "output_path": "path/to/processed/track.wav",  // Only present on success
    "message": "Processing message"
}
```

## Error Handling

The server will log all errors to the console and return appropriate error messages to the C++ plugin.
