from flask import Flask
from flask_mysqldb import MySQL
from .routes import setup_routes
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    # MySQL Config
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'admin2025'
    app.config['MYSQL_DB'] = 'simple_db'

    mysql = MySQL(app)

    setup_routes(app, mysql)

    return app
