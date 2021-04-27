from appPackage.models import db
from appPackage.models.UserModel import user
from appPackage.models.MachineModel import machine
from appPackage.models.ComponentModel import component
from appPackage.models.UtilizationModel import utilization
from appPackage.models.PurchaseModel import purchase
from appPackage.controllers.LoginController import loginForm
from appPackage.routes.routes import *
from flask import render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange

class registerForm(FlaskForm):
	nameUser = StringField('Nombre completo', [DataRequired(message='Debe llenar este campo'), Length(min=1, message='Ingresar un nombre valido')])
	username = StringField('Usuario', [DataRequired(message='Debe llenar este campo'), Length(min=1, message='Ingresar un nombre de usuario valido')])
	typeUser = SelectField('Tipo de usuario', choices=[('2', 'Encargado'), ('3', 'Tecnico')])
	password = PasswordField('Contraseña', [DataRequired(message='Debe llenar este campo'), Length(min=8, message="La contraseña debe ser almenos de 8 caracteres"), EqualTo('confirm', message='Las contraseñas deben coincidir')])
	confirm = PasswordField('Confirmar contraseña', [DataRequired(message='Debe llenar este campo'), Length(min=8, message="La contraseña debe ser almenos de 8 caracteres")])

class RegisterController():
	def __init__(self):
		pass
		
	def registerRoute(self, request):
		form = registerForm(request.form) # Creacion del formulario
		formLogout = loginForm()
		if request.method == 'POST' and form.validate():
			userTemp = db.session.query(user).filter(user.nameUser == request.form['nameUser']).first()
			if userTemp: # error de nombre
				flash('Error: Ya existe una cuenta registrada a ese nombre', 'WA')
				return render_template('register.html', formLogout=formLogout, form=form)
			userTemp = db.session.query(user).filter(user.username == request.form['username']).first()
			if userTemp: # error de nombre de usuario
				flash('Error: Ya existe una cuenta registrada a ese nombre de usuario', 'WA')
				return render_template('register.html', formLogout=formLogout, form=form)
			userNuevo = user(nameUser=request.form['nameUser'], username=request.form['username'], typeUser=request.form['typeUser'])
			userNuevo.set_password(request.form['password'])
			db.session.add(userNuevo)
			db.session.commit() 
			flash('Usuario registrado exitosamente', 'AC')
			return redirect(url_for('homeRoute'))
		else:
			return render_template('register.html', formLogout=formLogout, form=form)

