from appPackage import app, login_manager
from .models import db, user, machine, component, utilization, purchase
from .formsValidation import loginForm, registerForm
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, logout_user, current_user, login_user

@login_manager.user_loader
def load_user(user_id):
	return user.query.get(user_id)

@app.route('/login', methods=["GET", "POST"])
def loginRoute():
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
		flash('tdo bien', 'AC')
		return redirect(url_for('homeRoute'))
	return render_template('login.html', form=form)

@app.route('/logout', methods=["POST"])
@login_required
def logoutRoute():
	form = loginForm(request.form) # Creacion del formulario
	logout_user()
	return redirect(url_for('loginRoute'))

@app.route('/', methods=["GET"])
@app.route('/home', methods=["GET"])
@login_required
def homeRoute():
	form = loginForm()
	return render_template('home.html', formLogout=form, current_user=current_user)

@app.route('/registro', methods=["GET", "POST"])
def registerRoute():
	form = registerForm(request.form) # Creacion del formulario
	if request.method == 'POST' and form.validate():
		userTemp = db.session.query(user).filter(user.nameUser == request.form['nameUser']).first()
		if userTemp: # error de nombre
			flash('Error: Ya existe una cuenta registra a ese nombre', 'WA')
			return render_template('register.html', form=form)
		userTemp = db.session.query(user).filter(user.username == request.form['username']).first()
		if userTemp: # error de nombre de usuario
			flash('Error: Ya existe una cuenta registra a ese nombre de usuario', 'WA')
			return render_template('register.html', form=form)
		userNuevo = user(nameUser=request.form['nameUser'], username=request.form['username'], typeUser=request.form['typeUser'])
		userNuevo.set_password(request.form['password'])
		db.session.add(userNuevo)
		db.session.commit() 
		flash('Usuario registrado exitosamente', 'AC')
		return redirect(url_for('homeRoute'))
	else:
		return render_template('register.html', form=form)

@app.route('/registroMaquina', methods=["GET", "POST"])
@login_required
def registerMachineRoute():
	return 'registrar maquina'

@app.route('/registroComponente', methods=["GET", "POST"])
@login_required
def registerComponentRoute():
	return 'registrar componente'

@app.route('/actualizar', methods=["GET", "POST"])
@login_required
def updateRoute():
	return 'actualizar datos'

@app.route('/stock', methods=["GET", "POST"])
@login_required
def stockRoute():
	return 'registrar stock'