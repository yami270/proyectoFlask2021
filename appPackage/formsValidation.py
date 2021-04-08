from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo

class loginForm(FlaskForm):
	username = StringField('Usuario', [DataRequired(message='Debe llenar este campo'), Length(min=1, message='Ingresar un nombre de usuario valido')])
	password = PasswordField('Contraseña', [DataRequired(message='Debe llenar este campo'), Length(min=8, message="La contraseña debe ser almenos de 8 caracteres")])

class registerForm(FlaskForm):
	nameUser = StringField('Nombre completo', [DataRequired(message='Debe llenar este campo'), Length(min=1, message='Ingresar un nombre valido')])
	username = StringField('Usuario', [DataRequired(message='Debe llenar este campo'), Length(min=1, message='Ingresar un nombre de usuario valido')])
	typeUser = SelectField('Tipo de usuario', choices=[('2', 'Encargado'), ('3', 'Tecnico')])
	password = PasswordField('Contraseña', [DataRequired(message='Debe llenar este campo'), Length(min=8, message="La contraseña debe ser almenos de 8 caracteres"), EqualTo('confirm', message='Las contraseñas deben coincidir')])
	confirm = PasswordField('Confirmar contraseña', [DataRequired(message='Debe llenar este campo'), Length(min=8, message="La contraseña debe ser almenos de 8 caracteres")])
