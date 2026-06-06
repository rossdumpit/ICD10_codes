ICD10 Search Tool
Overview

This is a local desktop application that provides a searchable interface for ICD-10 related datasets. It uses a Python backend with FastAPI and a simple HTML frontend, packaged into a Windows executable for easy use.

Features
Search across multiple ICD-10 related CSV datasets
Simple web-based interface
Runs locally on your machine
Packaged as a Windows desktop executable
No external database required
Project Structure
run_app.py - Entry point for the desktop application
app.py - FastAPI backend server
search.py - Search logic for datasets
loader.py - Loads CSV data into memory
front.html - Frontend user interface
*.csv - Data files used for search
How It Works
The executable starts a local FastAPI server.
The server loads CSV datasets into memory.
A local webview window opens showing the interface.
User searches are sent to the backend API.
Results are returned dynamically from loaded datasets.
Running Locally (Development)

If running from source:

python run_app.py
Building the Executable (GitHub Actions)

The project uses GitHub Actions to automatically build a Windows executable.

After pushing to the repository:

Go to the Actions tab
Wait for the build to complete
Download the artifact containing the executable
Requirements

If running locally:

Python 3.11+
FastAPI
Uvicorn
pywebview

Install dependencies:

pip install fastapi uvicorn pywebview
Notes
The executable is Windows-only.
CSV files must be included for the application to function.
The app runs locally and does not require internet access after launch.
