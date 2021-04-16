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
	return myLoginController.loginRoute(request)

@app.route('/logout', methods=["POST"])
@login_required
def logoutRoute():
	return myLoginController.logoutRoute(request)

@app.route('/', methods=["GET"])
@app.route('/home', methods=["GET"])
@login_required
def homeRoute():
	return myLoginController.homeRoute()

@app.route('/registro', methods=["GET", "POST"])
def registerRoute():
	return myRegisterController.registerRoute(request)


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

from appPackage.controllers.LoginController import LoginController 
myLoginController = LoginController()

from appPackage.controllers.RegisterController import RegisterController 
myRegisterController = RegisterController()