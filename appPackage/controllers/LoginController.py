from appPackage.models import db, user, machine, component, utilization, purchase
from appPackage.formsValidation import loginForm, registerForm
from appPackage.routes.routes import *
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, logout_user, current_user, login_user

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
