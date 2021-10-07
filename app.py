from flask import Flask

def create_app():

    app = Flask(__name__)
    from views import main

    app.register_blueprint(main)

    return app

"""
@app.route('/')
def hola_mundo():
    return '<h1>Hola, Mundo! 2--</h1>'

@app.route('/otrapagina')
def otrapagina():
    return '<h1>Otra página.</h1>'"""   