from flask import Flask
from app.routes import app_login
from app.config import Config

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(app_login)
    app.config.from_object(Config)
    app.run(host='127.0.0.4', port=5001)

