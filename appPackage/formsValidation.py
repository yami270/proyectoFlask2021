from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange

class loginForm(FlaskForm):
	username = StringField('Usuario', [DataRequired(message='Debe llenar este campo'), Length(min=1, message='Ingresar un nombre de usuario valido')])
	password = PasswordField('Contraseña', [DataRequired(message='Debe llenar este campo'), Length(min=8, message="La contraseña debe ser almenos de 8 caracteres")])

class registerForm(FlaskForm):
	nameUser = StringField('Nombre completo', [DataRequired(message='Debe llenar este campo'), Length(min=1, message='Ingresar un nombre valido')])
	username = StringField('Usuario', [DataRequired(message='Debe llenar este campo'), Length(min=1, message='Ingresar un nombre de usuario valido')])
	typeUser = SelectField('Tipo de usuario', choices=[('2', 'Encargado'), ('3', 'Tecnico')])
	password = PasswordField('Contraseña', [DataRequired(message='Debe llenar este campo'), Length(min=8, message="La contraseña debe ser almenos de 8 caracteres"), EqualTo('confirm', message='Las contraseñas deben coincidir')])
	confirm = PasswordField('Confirmar contraseña', [DataRequired(message='Debe llenar este campo'), Length(min=8, message="La contraseña debe ser almenos de 8 caracteres")])

class machineForm(FlaskForm):
	nameMachine = StringField('Nombre maquina', [DataRequired(message='Debe llenar este campo'), Length(min=1, message='Ingresar un nombre valido')])
	descriptionMachine = TextAreaField('Descripcion')

class componentForm(FlaskForm):
	codeMachine = SelectField('Nombre Maquina', coerce=int)
	nameComponent = StringField('Nombre componente', [DataRequired(message='Debe llenar este campo'), Length(min=1, message='Ingresar un nombre valido')])
	typeComponent = SelectField('Tipo de componente', choices=[('1', 'Electrico'), ('2', 'Mecanico'), ('3', 'Neumatico'), ('4', 'Hidraulico'), ('5', 'Quimico')])
	priority = SelectField('Prioridad', choices=[('1', 'A'), ('2', 'B'), ('3', 'C')])
	notes = TextAreaField('Notas para el tecnico')
	currentStock = IntegerField('Cantidad Stock', [DataRequired(message='Debe llenar este campo'), NumberRange(min=1, message='Ingresar un monto valido')])
	minimumStock = IntegerField('Cantidad minima', [DataRequired(message='Debe llenar este campo'), NumberRange(min=1, message='Ingresar un monto valido')])
	date = DateField('Fecha de registro', [DataRequired(message='Debe llenar este campo')])

class stockForm(FlaskForm):
	codeComponent = SelectField('Nombre Componente', coerce=int)
	amount = IntegerField('Cantidad', [DataRequired(message='Debe llenar este campo'), NumberRange(min=1, message='Ingresar un monto valido')])
	date = DateField('Fecha registro', [DataRequired(message='Debe llenar este campo')])
