from flask import blueprints, render_template, request
from forms import frmRegistrar

main=blueprints.Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('Inicio-wtf.html')

@main.route('/login')
def loguin():
    return render_template('Login.html')

@main.route('/registro', methods=["GET", "POST"])
def registro():
    if request.method == 'POST':
        return 'POST'
    
    x = frmRegistrar()
    return render_template('Registro-wtf.html', form=x)

@main.route('/restablecercontraseña')
def restcontr():
    return render_template('Restablecer Contraseña.html')
