import os

from flask import Flask
from flask_cors import CORS
from palette import bp as palette_bp
from image import bp as image_bp
from dotenv import load_dotenv


load_dotenv()

ENV = os.getenv("ENV")
SERVER_PORT = os.getenv("SERVER_PORT")
FRONTEND_PORT = os.getenv("FRONTEND_PORT")

is_development = ENV == "development"
frontend_url = (
    f"http://localhost:{FRONTEND_PORT}"
    if is_development
    else os.getenv("PROD_FRONTEND_URL")
)

app = Flask(__name__)
app.register_blueprint(palette_bp)
app.register_blueprint(image_bp)

CORS(app, origins=frontend_url)

if __name__ == "__main__":
    if is_development and SERVER_PORT:
        app.run(debug=is_development, port=int(SERVER_PORT))
    else:
        app.run(debug=is_development)
