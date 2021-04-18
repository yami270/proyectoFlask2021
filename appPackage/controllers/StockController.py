from appPackage.models import db, user, machine, component, utilization, purchase
from appPackage.formsValidation import loginForm, registerForm, machineForm, componentForm, stockForm
from appPackage.routes import *
from flask import render_template, request, redirect, url_for, flash

class StockController():
	def __init__(self):
		pass

	def stockRoute(self, request):
		formPurchase = stockForm(request.form) # Creacion del formulario
		formPurchase.codeComponent.choices = [(g.id, g.machine.nameMachine+" : "+g.nameComponent) for g in db.session.query(component)]
		formUtilization = formPurchase
		formLogout = loginForm()
		return render_template('stock.html', formLogout=formLogout, formPurchase=formPurchase, formUtilization=formUtilization)
