from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

class loginForm(Form):
	username = StringField('Usuario', [DataRequired(message='Debe llenar este campo'), Length(min=1, message='Ingresar un nombre de usuario valido')])
	password = PasswordField('Contraseña', [DataRequired(message='Debe llenar este campo'), Length(min=8, message="La contraseña debe ser almenos de 8 caracteres")])
