@echo off

:: Check if Python is installed
echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3.8 or higher.
    exit /b 1
)

:: Create virtual environment
echo Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo Failed to create virtual environment.
    exit /b 1
)

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    exit /b 1
)

:: Install dependencies
echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install dependencies.
    exit /b 1
)

:: Install development tools
echo Installing development tools...
pip install pytest black isort flake8
if %errorlevel% neq 0 (
    echo Failed to install development tools.
    exit /b 1
)

:: Copy environment file
echo Copying environment file...
if not exist .env (
    copy .env.example .env
)

:: Create directories
echo Creating necessary directories...
mkdir temp
mkdir processed
mkdir logs

:: Setup complete
echo Setup complete!
echo Virtual environment is ready to use.
echo Activate it with: venv\Scripts\activate.bat
