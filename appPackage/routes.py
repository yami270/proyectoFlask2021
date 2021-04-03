from appPackage import app, login_manager
from .models import db, user, machine, component, utilization, purchase
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, logout_user, current_user, login_user

@login_manager.user_loader
def load_user(user_id):
	return user.query.get(user_id)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/login', methods=["GET", "POST"])
def loginRoute():
	if request.method == 'GET':
		return 'esto es el login de la vista'
	else:
		#solo es una especulacion

		# form = SignupForm()
  #   if form.validate_on_submit():
  #     existing_user = User.query.filter_by(email=form.email.data).first()
  #     if existing_user is None:
  #       user = User(name=form.name.data, email=form.email.data, website=form.website.data)
  #     user.set_password(form.password.data)
  #     db.session.add(user)
  #     db.session.commit()  # Create new user
  #     login_user(user)  # Log in as newly created user
  #     return redirect(url_for('main_bp.dashboard'))
  #   flash('A user already exists with that email address.')

		return 'esto es el login del post'

@app.route('/home')
def homeRoute():
	return 'este es el home'

@app.route('/registro', methods=["GET", "POST"])
def register():
	if request.method == 'POST':
		return 'esto es from de registro'
	else:
		userNuevo = user(nameUser='migufe6l4', username='yamri2d77_', typeUser=1)
		userNuevo.set_password('miau')
		db.session.add(userNuevo)
		db.session.commit()  # Create new user
		#login_user(userNuevo) #logea al nuevo usuario
		return 'esto es el login del post'

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