from flask import blueprints, render_template

main=blueprints.Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('Pagina de Inicio.html')

@main.route('/loguin')
def loguin():
    return render_template('Loguin.html')

@main.route('/registro')
def registro():
    return render_template('Registro.html')