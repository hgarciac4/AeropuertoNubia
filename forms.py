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