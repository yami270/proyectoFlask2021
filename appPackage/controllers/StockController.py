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

class stockForm(FlaskForm):
	codeComponent = SelectField('Nombre Componente', coerce=int)
	amount = IntegerField('Cantidad', [DataRequired(message='Debe llenar este campo'), NumberRange(min=1, message='Ingresar un monto valido')])
	date = DateField('Fecha registro', [DataRequired(message='Debe llenar este campo')])

class StockController():
	def __init__(self):
		pass

	def stockRoute(self, request):
		formPurchase = stockForm(request.form) # Creacion del formulario
		formPurchase.codeComponent.choices = [(g.id, g.machine.nameMachine+" : "+g.nameComponent) for g in db.session.query(component)]
		formUtilization = formPurchase
		formLogout = loginForm()
		return render_template('stock.html', formLogout=formLogout, formPurchase=formPurchase, formUtilization=formUtilization)

	def stockPurchaseRoute(self, request):
		formPurchase = stockForm(request.form) # Creacion del formulario
		formPurchase.codeComponent.choices = [(g.id, g.machine.nameMachine+" : "+g.nameComponent) for g in db.session.query(component)]
		if formPurchase.validate():
			purchaseNuevo = purchase(codeComponent=request.form['codeComponent'], date=request.form['date'], amount=request.form['amount'])
			db.session.add(purchaseNuevo)
			componentUpdate = db.session.query(component).filter(component.id == request.form['codeComponent']).first()
			componentUpdate.currentStock += int(request.form['amount'])
			db.session.commit() 
			flash('Compra registrada exitosamente', 'AC')
			return redirect(url_for('homeRoute'))
		else:
			flash('Datos invalidos', 'WA')
			return redirect(url_for('stockRoute'))

	def stockUtilizationRoute(self, request):
		formUtilization = stockForm(request.form) # Creacion del formulario
		formUtilization.codeComponent.choices = [(g.id, g.machine.nameMachine+" : "+g.nameComponent) for g in db.session.query(component)]
		if formUtilization.validate():
			componentUpdate = db.session.query(component).filter(component.id == request.form['codeComponent']).first()
			if componentUpdate.currentStock < int(request.form['amount']):
				flash('No existe la cantidad requerida en almacenes', 'WA')
				return redirect(url_for('stockRoute'))
			componentUpdate.currentStock -= int(request.form['amount'])
			utilizationNuevo = utilization(codeComponent=request.form['codeComponent'], date=request.form['date'], amount=request.form['amount'])
			db.session.add(utilizationNuevo)
			db.session.commit() 
			flash('Uso registrado exitosamente', 'AC')
			return redirect(url_for('homeRoute'))
		else:
			flash('Datos invalidos', 'WA')
			return redirect(url_for('stockRoute'))