# My MISTY1818 Python App with Flask

This application is built using Flask. Follow the instructions below to set up the environment and run the application.

## Prerequisites

- You need to install Python 3.10.9 or higher.

  ```bash
  sudo apt install python3.10.9
  mkdir misty1818
  cd misty1818
  python3 -m venv .venv
  . .venv/bin/activate
  ```

## Installation

To install the required packages, run the following commands:

```bash
python -m pip install Flask
python -m pip install requests
python -m pip install python-dotenv
```

## Configuration

In the `index.html` file, locate line 98 and change the `http://127.0.0.1:5000` to your own endpoint.

## Running the App

To activate the app, you need to write the following command in the terminal:

```bash
python app.py
```

## Important Note

Please make sure to follow your provider's specific instructions on how to install and deploy Python apps with Flask.
## For DigitalOcean Users

If you are using DigitalOcean servers, please follow the guide available at the following link to set up your Flask and Python environment:

[How to Create Your First Web Application Using Flask and Python 3 on DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3)