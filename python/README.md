# MasterMatcher Python Backend

This directory contains the Python backend for the MasterMatcher VST plugin.

## Project Structure
```
python/
├── venv/                 # Virtual environment
├── src/                 # Source code
├── tests/               # Test files
├── logs/               # Log files
├── temp/               # Temporary files
├── processed/          # Processed audio files
├── .env                # Environment variables (copy from .env.example)
├── .env.example        # Environment template
├── setup.py            # Package setup
├── pyproject.toml      # Project configuration
├── requirements.txt    # Python dependencies
├── setup_env.bat       # Windows setup script
└── README.md          # This file
```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/albertjgonzalez/MasterMatcherVST.git
```

2. Navigate to the Python directory:
```bash
cd MasterMatcherVST/python
```

3. Run the setup script:
```bash
python/setup_env.bat
```

The script will:
- Create and activate a virtual environment
- Install all dependencies
- Set up necessary directories
- Copy the environment file template

4. Configure environment variables:
- Copy `.env.example` to `.env`
- Modify settings as needed

## Development

### Running Tests
```bash
pytest tests/
```

### Formatting Code
```bash
black .
isort .
```

### Linting
```bash
flake8 .
```

## Environment Variables

Create a `.env` file based on `.env.example` with the following variables:
```env
# Output directory for processed audio files
OUTPUT_DIR=processed

# Log configuration
LOG_LEVEL=INFO
LOG_FILE=mastermatcher.log

# Processing settings
MAX_PROCESSING_TIME=300  # Maximum processing time in seconds
TEMP_DIR=temp

# Monitoring settings
MONITOR_INTERVAL=1  # Monitoring interval in seconds
MAX_RETRIES=3  # Maximum number of retries for failed operations

# API settings (if using REST API)
API_HOST=127.0.0.1
API_PORT=8000

# Security settings
SECRET_KEY=your-secret-key-here  # Change this in production
JWT_EXPIRATION=3600  # Token expiration time in seconds

# Debug settings
DEBUG=False
PROFILE=False
```

## Running the Server

1. Activate the virtual environment:
```bash
venv\Scripts\activate
```

2. Run the server:
```bash
python src/server.py
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
    "output_path": "path/to/processed/track.wav",  # Only present on success
    "message": "Processing message"
}
```

## Error Handling

The server will:
- Log all errors to `logs/mastermatcher.log`
- Return appropriate error messages to the C++ plugin
- Retry failed operations up to MAX_RETRIES times
- Monitor processing time and terminate if it exceeds MAX_PROCESSING_TIME
