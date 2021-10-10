from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, DateField, BooleanField, RadioField
from wtforms.validators import DataRequired, Email, Length

class frmRegistrar(FlaskForm):
    identificacion = IntegerField("identificacion", validators=[
        DataRequired()
    ])
    nombre = StringField("Nombre", validators=[
        DataRequired(),
        Length(max=10, min=3)
    ])
    apellidos = StringField("Apellidos", validators=[
        DataRequired(),
        Length(max=30, min=3)
    ])
    fechaNacimiento = DateField(
        "Fecha de Nacimiento",
        format = '%d/%m/%y'
    )
    genero = RadioField("Genero", choices=[('M','Masculino'),('F','Femenino'),('O','Otro')], validators=[
        DataRequired()
    ])
    telefono = IntegerField("Telefono")
    correo = StringField("Correo", validators=[
        DataRequired(),
        Email()
    ])
    contraseña = PasswordField("Contraseña", validators=[
        DataRequired()
    ])
    condiciones = BooleanField("")
    registrar = SubmitField("Registrar")

class frmLogin(FlaskForm):
    correo = StringField("Email", validators=[
        DataRequired(),
        Email()
    ])
    contraseña = PasswordField("Contraseña", validators=[
        DataRequired()
    ])
    iniciarsesion = SubmitField("Iniciar Sesion")

class frmRecordarContraseña(FlaskForm):
    dato = StringField("Dato de Identificación:", validators=[
        DataRequired()
    ])
    newContraseña = PasswordField("Nueva Contraseña", validators=[
        DataRequired()
    ])
    newContraseña2 = PasswordField("Confirmar Contraseña", validators=[
        DataRequired()
    ])
    enviar = SubmitField("Enviar")