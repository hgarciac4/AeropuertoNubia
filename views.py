from flask import blueprints, render_template, request, url_for, redirect
from forms import frmRegistrar, frmLogin, frmRecordarContraseña

main=blueprints.Blueprint('main', __name__)

@main.route('/', method="GET")
def index():
    return render_template('Inicio.html')


@main.route('/login', methods=["GET"])
@main.route('/login/<tipo>', methods=["GET", "POST"])
def login(tipo):
    x = frmLogin()
    
    if request.method == 'POST':
        return render_template("main.dashboard", tipo=tipo)
        
    return render_template('Login-wtf.html', tipo=tipo, form=x)
    

@main.route('/dashboard', methods=["GET", "POST"])
@main.route('/dashboard/<tipo>', methods=["GET", "POST"])
def dashboard(tipo=None):
    if request.method == 'POST':
        return redirect(url_for("main.login"))
    
    return render_template('Dashboard.html', tipo=tipo)


@main.route('/consultavuelo', methods=["GET", "POST"])
@main.route('/consultavuelo/<tipo>', methods=["GET", "POST"])
def consultaVuelo(tipo=None):
    if tipo == None:
        return redirect(url_for("main.login"))

    return render_template('Consultar.html', tipo=tipo)


@main.route('/calificaVuelo', methods=["GET", "POST"])
@main.route('/calificavuelo/<tipo>', methods=["GET", "POST"])
def calificaVuelo(tipo=None):
    if tipo == None:
        return redirect(url_for("main.login"))
        
    return render_template('Calificanos.html', tipo=tipo)


@main.route('/reservaVuelo', methods=["GET", "POST"])
@main.route('/reservaVuelo/<tipo>', methods=["GET", "POST"])
def reservaVuelo(tipo=None):
    if tipo == None:
        return redirect(url_for("main.login"))
        
    return render_template('Reservar.html', tipo=tipo)


@main.route('/registro', methods=["GET", "POST"])
def registro():
    x = frmRegistrar()    
    if request.method == 'POST':
        return render_template('Registro-wtf.html', form=x)

    return redirect(url_for('main.inicio'))


@main.route('/restaurar_contraseña', methods=["GET", "POST"])
def restaurar_contraseña():
    x = frmRecordarContraseña()
    if request.method == 'POST':
        return render_template('RestablecerContraseña-wtf.html', form=x)

    return redirect(url_for('main.inicio'))
