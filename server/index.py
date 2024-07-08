import os
from flask import Flask
from flask_cors import CORS
from api.image import bp as image_bp
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "production")
SERVER_PORT = os.getenv("SERVER_PORT")
FRONTEND_PORT = os.getenv("FRONTEND_PORT")
PROD_FRONTEND_URL = os.getenv("PROD_FRONTEND_URL")

is_development = ENV == "development"
frontend_url = (
    f"http://localhost:{FRONTEND_PORT}" if is_development else PROD_FRONTEND_URL
)

app = Flask(__name__)
app.register_blueprint(image_bp)

# Use a list for origins
CORS(app, origins=[frontend_url])

if __name__ == "__main__":
    if is_development and SERVER_PORT:
        app.run(debug=True, port=int(SERVER_PORT))
    else:
        app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
