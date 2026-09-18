from flask import Flask
from app.api.upload import upload_bp


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return {
            "status": "ok",
            "service": "DarkGPT backend",
            "message": "Backend is running"
        }

    app.register_blueprint(upload_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=10000)
