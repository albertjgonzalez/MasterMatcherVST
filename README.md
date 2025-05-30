# MasterMatcher VST Plugin

A VST plugin that uses Matchering's AI audio mastering algorithms to analyze and match audio tracks in your DAW in real-time.

## Features
- Real-time audio processing
- Reference track matching
- AI-powered mastering using Matchering
- JUCE-based UI with Python backend
- Cross-platform support
- 32-bit float audio processing
- Support for 44.1kHz, 48kHz, and 96kHz sample rates
- Stereo audio processing
- Intensity and reference weight controls

## Requirements
- JUCE framework (latest version)
- C++17 or later
- Python 3.8+
- Matchering library (2.0.6)
- Audio host (DAW) supporting VST3 plugins
- Git for version control

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mastermatcher-vst.git
   cd mastermatcher-vst
   ```

2. Set up Python environment:
   ```bash
   cd python
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Build the plugin:
   - Open `MasterMatcher.jucer` in Projucer
   - Generate project files for your IDE
   - Build the project

4. Install in your DAW:
   - Copy the built VST3 file to your DAW's plugin directory
   - Restart your DAW

## Usage
1. Load your audio track:
   - Connect the plugin to your audio track in the DAW
   - The plugin will automatically receive the audio stream

2. Load a reference track:
   - Click the "Load Reference" button
   - Select a WAV file (32-bit float, 44.1kHz or 48kHz, minimum 30 seconds)

3. Configure processing:
   - Adjust the "Intensity" slider (0-100)
   - Adjust the "Reference Weight" slider (0-100)
   - Choose between "Fast" or "Accurate" processing mode
   - Set the lookahead time

4. Process audio:
   - Click the "Master" button to start real-time processing
   - Use the preview button to compare before/after
   - Save processed audio using the export button

## Build Instructions
1. Set up Python environment:
   - Navigate to `python` directory
   - Run `setup_env.bat` to create and configure virtual environment
   - Install required packages from `requirements.txt`

2. Build Matchering:
   - Clone Matchering repository
   - Build as static library
   - Configure include paths in CMake

3. Build Plugin:
   - Open `MasterMatcher.jucer` in Projucer
   - Configure build settings
   - Generate project files
   - Build in your IDE

## Project Structure
```
mastermatcher-vst/
├── PluginEditor.cpp
├── PluginEditor.h
├── PluginProcessor.cpp
├── PluginProcessor.h
├── MasterMatcher.jucer
├── python/
│   ├── src/
│   │   ├── processor.py
│   │   ├── server.py
│   │   └── protocol.py
│   ├── requirements.txt
│   ├── setup_env.bat
│   └── .env.example
└── docs/
    ├── technical_integration.md
    ├── data_flow.md
    └── task_breakdown.md
```

## Development
- Python backend handles audio processing using Matchering
- C++ frontend manages real-time audio processing
- Communication between Python and C++ using JSON protocol
- Comprehensive error handling and logging system

## License
MIT License

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Support
- Report issues through GitHub Issues
- Contact [your email] for support
