i Pegasus Detection API
The purpose of the project is to create a softaware that detect the spyware that enable every user to know if their gadget has pegasus which will enable them to detect it and also uninstall the spyware for the user.

This project is designed to detect and analyze Pegasus spyware using various methods including network traffic analysis, memory forensics, file system analysis, and mobile device analysis.

## Requirements

- Python 3.8+
- Docker (optional)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pegasus_detection_api.git
   cd pegasus_detection_api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your secret key:
   ```
   SECRET_KEY=your_secret_key
   ```

5. Run the application:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --log-level info
   ```

6. (Optional) Build and run using Docker:
   ```bash
   docker build -t pegasus_detection_api .
   docker run -p 8000:8000 pegasus_detection_api
   ```

## Endpoints

- `/network/analyze`: Analyze network traffic
- `/memory/analyze`: Analyze memory dump
- `/file/analyze`: Analyze file system
- `/mobile/analyze`: Analyze mobile device backup

