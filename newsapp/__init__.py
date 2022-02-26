from flask import Flask
from config import config_options

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    #blueprint register
    from .views import views
    app.register_blueprint(views, url_prefix = '/')
    
    # setting config
    # from .request import configure_request
    # configure_request(app)

    return app