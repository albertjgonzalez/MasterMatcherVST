from setuptools import setup, find_packages

setup(
    name="mastermatcher",
    version="0.1.0",
    description="Python backend for MasterMatcher VST plugin",
    author="Left Ear Audio",
    author_email="",
    packages=find_packages(),
    install_requires=[
        'matchering>=3.0.0',
        'numpy>=1.21.0',
        'scipy>=1.7.0',
        'soundfile>=0.10.3',
        'python-dotenv>=0.19.0',
        'watchdog>=2.1.0',
        'psutil>=5.8.0',
        'pydub>=0.25.1',
        'requests>=2.26.0',
        'python-multipart>=0.0.6',
        'python-jose>=3.3.0',
        'fastapi>=0.68.0',
        'uvicorn>=0.15.0'
    ],
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
