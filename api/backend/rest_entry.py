import logging
import os

logging.basicConfig(level=logging.DEBUG)

from flask import Flask
from backend.db_connection import db
from backend.city_council.city_council_routes import city_council
from backend.immigration_official.immigration_officer_routes import immigration_official
from backend.migrant.migrant_routes import migrant
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    # Load environment variables
    load_dotenv()
    testvar = os.getenv('TEST_VAR')
    app.logger.info(f'testvar is {testvar}')

    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    # app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # # these are for the DB object to be able to connect to MySQL. 
    # app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER')
    app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_ROOT_PASSWORD')
    app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST')
    app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('DB_PORT'))
    app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_NAME')  # Change this to your DB name

    # Initialize the database object with the settings above. 
    db.init_app(app)

    # Add the default route
    # Can be accessed from a web browser
    # http://ip_address:port/
    # Example: localhost:8001
    @app.route("/")
    def welcome():
        return "<h1>Welcome to the Summer 2024 Belgium DoC Boilerplate App</h1>"
    
    # Example route for testing streamlit
    @app.route("/data")
    def getData():
        data = {              
                "user1": {
                    "Name": "Mark Fontenot",
                    "Course": "CS 3200",
                },
                "user2": {
                    "Name": "Eric Gerber",
                    "Course": "DS 3000",
                }
            }
        return data
    
    app.logger.info('current_app(): registering blueprints with app object.')
    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    app.register_blueprint(city_council,   url_prefix='/c')
    app.register_blueprint(immigration_official,    url_prefix='/i')
    app.register_blueprint(migrant,   url_prefix='/m')


    # Don't forget to return the app object
    return app

