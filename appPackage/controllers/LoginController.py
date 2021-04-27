from appPackage.models import db
from appPackage.models.UserModel import user
from appPackage.models.MachineModel import machine
from appPackage.models.ComponentModel import component
from appPackage.models.UtilizationModel import utilization
from appPackage.models.PurchaseModel import purchase
from appPackage.routes.routes import *
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, logout_user, current_user, login_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange

class loginForm(FlaskForm):
	username = StringField('Usuario', [DataRequired(message='Debe llenar este campo'), Length(min=1, message='Ingresar un nombre de usuario valido')])
	password = PasswordField('Contraseña', [DataRequired(message='Debe llenar este campo'), Length(min=8, message="La contraseña debe ser almenos de 8 caracteres")])

class LoginController():
	def __init__(self):
		pass

	def loginRoute(self, request):
		if current_user.is_authenticated:
			return redirect(url_for('homeRoute'))
		form = loginForm(request.form) # Creacion del formulario
		if request.method == 'POST' and form.validate():
			userTemp = db.session.query(user).filter(user.username == request.form['username']).first()
			if not userTemp or not userTemp.check_password(request.form['password']):
				flash('Error: No existe una cuenta con los datos ingresados', 'WA')
				return render_template('login.html', form=form)
			# inicio de session
			login_user(userTemp)
			flash('Bienvenido', 'AC')
			return redirect(url_for('homeRoute'))
		return render_template('login.html', form=form)

	def logoutRoute(self, request):
		form = loginForm(request.form) # Creacion del formulario
		logout_user()
		return redirect(url_for('loginRoute'))

	def homeRoute(self):
		form = loginForm()
		dataComponent = db.session.query(component).order_by(component.codeMachine.asc())
		return render_template('home.html', formLogout=form, current_user=current_user, dataComponent=dataComponent)

	def user_loader(self, user_id):
		return user.query.get(user_id)