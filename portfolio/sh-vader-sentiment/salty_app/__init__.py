# __init__.py

import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
# from salty_app.models import db, migrate
from salty_app.routes.home_routes import home_routes


# Creating DataBase name in the current directory -- using relative filepath
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


# Defining Function "create_app"
def create_app():
    # Instantiating Flask App
    app = Flask(__name__)
    # Add CORS to app
    cors = CORS(app)

    # # Configures the DataBase w/ name specified by "DATABASE_URI"
    # app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    # # Initializes the DataBase
    # db.init_app(app)
    # # Migrates the app and DataBase
    # migrate.init_app(app, db)

    # Registering the "home_routes" blueprint
    app.register_blueprint(home_routes)

    # Returning / Running Flask App
    return app


# Factory pattern; Flask best practice -- creating and running app
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
