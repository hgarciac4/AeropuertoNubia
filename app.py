import os
from flask import Flask
# from flask_bootstrap import Bootstrap

def create_app():

    app = Flask(__name__)
    app.secret_key = os.urandom( 50 )

    from views import main

    # Bootstrap(app)
    app.register_blueprint(main)

    return app
