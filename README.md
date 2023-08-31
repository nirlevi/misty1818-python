# My MISTY1818 Python App with FastAPI

This application is built using FastAPI. Follow the instructions below to set up the environment and run the application.

## Prerequisites

- You need to install Python 3.10.9 or higher.

  ```bash
  sudo apt install python3.10.9
  ```

## Installation

To install the required packages, run the following commands:

```bash
python -m pip install fastapi
python -m pip install uvicorn
python -m pip install requests
python -m pip install python-dotenv
```

## Configuration

In the `index.html` file, locate line 98 and change the `http://127.0.0.1:5000` to your own endpoint.

## Running the App

To activate the app, you need to write the following command in the terminal:

```bash
uvicorn main:app --reload
```

## Important Note

Please make sure to follow your provider's specific instructions on how to install and deploy Python apps with Flask.