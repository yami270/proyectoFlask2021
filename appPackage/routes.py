from appPackage import app, login_manager
from .models import db, user, machine, component, utilization, purchase
from .formsValidation import loginForm, registerForm
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, logout_user, current_user, login_user

@login_manager.user_loader
def load_user(user_id):
	return user.query.get(user_id)

@app.route('/')
def index():
	return redirect(url_for('loginRoute'))

@app.route('/login', methods=["GET", "POST"])
def loginRoute():
	form = loginForm(request.form) # Creacion del formulario
	if request.method == 'POST' and form.validate():
		return redirect(url_for('homeRoute'))
	return render_template('login.html', form=form)

@app.route('/home')
def homeRoute():
	return render_template('home.html')

@app.route('/registro', methods=["GET", "POST"])
def register():
	form = registerForm(request.form) # Creacion del formulario
	if request.method == 'POST' and form.validate():
		return 'esto es from de registro valido'
	else:
		# userNuevo = user(nameUser='migufe6l4', username='yamri2d77_', typeUser=1)
		# userNuevo.set_password('miau')
		# db.session.add(userNuevo)
		# db.session.commit()  # Create new user
		# #login_user(userNuevo) #logea al nuevo usuario
		return render_template('register.html', form=form)

@app.route('/registroMaquina')
def registerMachineRoute():
	return 'registrar maquina'

@app.route('/registroComponente')
def registerComponentRoute():
	return 'registrar componente'

@app.route('/actualizar')
def updateRoute():
	return 'actualizar datos'

@app.route('/stock')
def stockRoute():
	return 'registrar stock'