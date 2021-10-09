from flask import blueprints, render_template, request, url_for, redirect
from forms import frmRegistrar

main=blueprints.Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('Inicio.html')


@main.route('/login', methods=["GET"])
def login():
    return render_template('Login.html')


@main.route('/registro', methods=["GET", "POST"])
def registro():
    if request.method == 'POST':
        return 'POST'
    
    x = frmRegistrar()
    return render_template('Registro-wtf.html', form=x)