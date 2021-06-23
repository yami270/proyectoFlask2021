from appPackage.models import db
from appPackage.models.MachineModel import machine
from appPackage.models.ComponentModel import component
from appPackage.models.PurchaseModel import purchase
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SelectField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange
from appPackage.controllers.LoginController import loginForm
from appPackage.routes.routes import *
from flask import render_template, request, redirect, url_for, flash
import json

class componentForm(FlaskForm):
	codeMachine = SelectField('Nombre Maquina', coerce=int)
	nameComponent = StringField('Nombre componente', [DataRequired(message='Debe llenar este campo'), Length(min=1, message='Ingresar un nombre valido')])
	typeComponent = SelectField('Tipo de componente', choices=[('1', 'Electrico'), ('2', 'Mecanico'), ('3', 'Neumatico'), ('4', 'Hidraulico'), ('5', 'Quimico')])
	priority = SelectField('Prioridad', choices=[('1', 'A'), ('2', 'B'), ('3', 'C')])
	notes = TextAreaField('Notas para el tecnico')
	currentStock = IntegerField('Cantidad Stock', [DataRequired(message='Debe llenar este campo'), NumberRange(min=1, message='Ingresar un monto valido')])
	minimumStock = IntegerField('Cantidad minima', [DataRequired(message='Debe llenar este campo'), NumberRange(min=1, message='Ingresar un monto valido')])
	date = DateField('Fecha de registro', [DataRequired(message='Debe llenar este campo')])

class componentUpdateForm(FlaskForm):
	nameComponent = StringField('Nombre componente', [DataRequired(message='Debe llenar este campo'), Length(min=1, message='Ingresar un nombre valido')])
	typeComponent = SelectField('Tipo de componente', choices=[('1', 'Electrico'), ('2', 'Mecanico'), ('3', 'Neumatico'), ('4', 'Hidraulico'), ('5', 'Quimico')])
	priority = SelectField('Prioridad', choices=[('1', 'A'), ('2', 'B'), ('3', 'C')])
	notes = TextAreaField('Notas para el tecnico')
	minimumStock = IntegerField('Cantidad minima', [DataRequired(message='Debe llenar este campo'), NumberRange(min=1, message='Ingresar un monto valido')])

class ComponentController():
	def __init__(self):
		pass

	def registerComponentRoute(self, request):
		if current_user.typeUser == 3:
			flash('Error 404: Ruta no encontrada', 'WA')
			return redirect(url_for('homeRoute'))
		form = componentForm(request.form) # Creacion del formulario
		form.codeMachine.choices = [(g.id, g.nameMachine) for g in db.session.query(machine)]
		formLogout = loginForm()
		if request.method == 'POST' and form.validate():
			componentTemp = db.session.query(component).filter(component.nameComponent == request.form['nameComponent']).first()
			if componentTemp: # error de nombre
				flash('Error: Ya existe un componente registrado a ese nombre', 'WA')
				return render_template('registerComponent.html', formLogout=formLogout, form=form)
			
			componentNuevo = component(codeMachine=request.form['codeMachine'], nameComponent=request.form['nameComponent'], typeComponent=request.form['typeComponent'], priority=request.form['priority'], notes=request.form['notes'], currentStock=request.form['currentStock'], minimumStock=request.form['minimumStock'])
			db.session.add(componentNuevo)
			componentTemp = db.session.query(component).filter(component.nameComponent == request.form['nameComponent']).first()
			purchaseNuevo = purchase(codeComponent=componentTemp.id, date=request.form['date'], amount=request.form['currentStock'])
			db.session.add(purchaseNuevo)
			db.session.commit() 
			flash('Componente registrado exitosamente', 'AC')
			return redirect(url_for('homeRoute'))
		else:
			return render_template('registerComponent.html', formLogout=formLogout, form=form)

	def updateComponentRoute(self, request):
		if current_user.typeUser == 3:
			flash('Error 404: Ruta no encontrada', 'WA')
			return redirect(url_for('homeRoute'))
		form = componentUpdateForm(request.form) # Creacion del formulario
		formLogout = loginForm()
		data = db.session.query(component).order_by(component.codeMachine.asc())
		if request.method == 'POST' and form.validate():
			componentTemp = db.session.query(component).filter(component.id == request.form['codeComponent']).first()
			if not componentTemp:
				flash('Error: No existe un componente registrado a ese nombre', 'WA')
				return render_template('updateComponent.html', formLogout=formLogout, form=form, data=data)
			componentDuplicate = db.session.query(component).filter(component.nameComponent == request.form['nameComponent']).filter(component.id != request.form['codeComponent']).first()
			if componentDuplicate: # error de nombre
				flash('Error: Ya existe un componente registrado a ese nombre', 'WA')
				return render_template('updateComponent.html', formLogout=formLogout, form=form, data=data)
			componentTemp.nameComponent = request.form['nameComponent']
			componentTemp.typeComponent = request.form['typeComponent']
			componentTemp.priority = request.form['priority']
			componentTemp.notes = request.form['notes']
			componentTemp.minimumStock = request.form['minimumStock']
			db.session.commit() 
			flash('Componente actualizado exitosamente', 'AC')
			return redirect(url_for('homeRoute'))
		else:
			return render_template('updateComponent.html', formLogout=formLogout, form=form, data=data)

	def viewComponentRoute(self, request):
		formLogout = loginForm()
		data = db.session.query(component).order_by(component.codeMachine.asc())
		return render_template('viewComponent.html', formLogout=formLogout, data=data)

	def getComponentRoute(self, request):
		dataRequest = request.json
		data = db.session.query(component).filter(component.id == dataRequest['codeComponent']).first()
		xxx = data.__dict__
		xxx.pop('_sa_instance_state', None)
		return json.dumps(xxx)