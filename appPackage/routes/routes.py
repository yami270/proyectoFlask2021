from appPackage import app, login_manager
from appPackage.models import db, user, machine, component, utilization, purchase
from appPackage.formsValidation import loginForm, registerForm
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
@login_required
def registerRoute():
	return myRegisterController.registerRoute(request)

@app.route('/registroMaquina', methods=["GET", "POST"])
@login_required
def registerMachineRoute():
	return myMachineController.registerMachineRoute(request)

@app.route('/registroComponente', methods=["GET", "POST"])
@login_required
def registerComponentRoute():
	return myComponentController.registerComponentRoute(request)

@app.route('/actualizarMaquina', methods=["GET", "POST"])
@login_required
def updateMachineRoute():
	return myMachineController.updateMachineRoute(request)

@app.route('/actualizarComponente', methods=["GET", "POST"])
@login_required
def updateComponentRoute():
	return myComponentController.updateComponentRoute(request)

@app.route('/stock', methods=["GET"])
@login_required
def stockRoute():
	return myStockController.stockRoute(request)

@app.route('/stock/compra', methods=["POST"])
@login_required
def stockPurchaseRoute():
	return myStockController.stockPurchaseRoute(request)

@app.route('/stock/uso', methods=["POST"])
@login_required
def stockUtilizationRoute():
	return myStockController.stockUtilizationRoute(request)

@app.route('/verMaquina', methods=["GET"])
@login_required
def viewMachineRoute():
	return myMachineController.viewMachineRoute(request)

@app.route('/verMaquina', methods=["POST"])
@login_required
def getMachineRoute():
	return myMachineController.getMachineRoute(request)

@app.route('/verComponente', methods=["GET"])
@login_required
def viewComponentRoute():
	return myComponentController.viewComponentRoute(request)

@app.route('/verComponente', methods=["POST"])
@login_required
def getComponentRoute():
	return myComponentController.getComponentRoute(request)

from appPackage.controllers.LoginController import LoginController 
myLoginController = LoginController()

from appPackage.controllers.RegisterController import RegisterController 
myRegisterController = RegisterController()

from appPackage.controllers.MachineController import MachineController 
myMachineController = MachineController()

from appPackage.controllers.ComponentController import ComponentController 
myComponentController = ComponentController()

from appPackage.controllers.StockController import StockController 
myStockController = StockController()