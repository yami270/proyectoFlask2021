from appPackage.models import db
from appPackage.models.UserModel import user
from appPackage.models.MachineModel import machine
from appPackage.models.ComponentModel import component
from appPackage.models.UtilizationModel import utilization
from appPackage.models.PurchaseModel import purchase
from appPackage.controllers.LoginController import loginForm
from appPackage.routes.routes import *
from flask import render_template, request, redirect, url_for, flash
import json
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SelectField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange

class machineForm(FlaskForm):
	nameMachine = StringField('Nombre maquina', [DataRequired(message='Debe llenar este campo'), Length(min=1, message='Ingresar un nombre valido')])
	descriptionMachine = TextAreaField('Descripcion')

class MachineController():
	def __init__(self):
		pass

	def registerMachineRoute(self, request):
		if current_user.typeUser == 3:
			flash('Error 404: Ruta no encontrada', 'WA')
			return redirect(url_for('homeRoute'))
		form = machineForm(request.form) # Creacion del formulario
		formLogout = loginForm()
		if request.method == 'POST' and form.validate():
			machineTemp = db.session.query(machine).filter(machine.nameMachine == request.form['nameMachine']).first()
			if machineTemp: # error de nombre
				flash('Error: Ya existe una maquina registrada a ese nombre', 'WA')
				return render_template('registerMachine.html', formLogout=formLogout, form=form)
			
			machineNuevo = machine(nameMachine=request.form['nameMachine'], descriptionMachine=request.form['descriptionMachine'])
			db.session.add(machineNuevo)
			db.session.commit() 
			flash('Maquina registrada exitosamente', 'AC')
			return redirect(url_for('homeRoute'))
		else:
			return render_template('registerMachine.html', formLogout=formLogout, form=form)

	def updateMachineRoute(self, request):
		if current_user.typeUser == 3:
			flash('Error 404: Ruta no encontrada', 'WA')
			return redirect(url_for('homeRoute'))
		form = machineForm(request.form) # Creacion del formulario
		formLogout = loginForm()
		if request.method == 'POST' and form.validate():
			machineTemp = db.session.query(machine).filter(machine.id == request.form['codeMachine']).first()
			if not machineTemp:
				flash('Error: No existe una maquina registrada a ese nombre', 'WA')
				data = db.session.query(machine.id, machine.nameMachine).order_by(machine.id.asc())
				return render_template('updateMachine.html', formLogout=formLogout, form=form, data=data)
			
			machineDuplicate = db.session.query(machine).filter(machine.nameMachine == request.form['nameMachine']).filter(machine.id != request.form['codeMachine']).first()
			if machineDuplicate: # error de nombre
				flash('Error: Ya existe una maquina registrada a ese nombre', 'WA')
				data = db.session.query(machine.id, machine.nameMachine).order_by(machine.id.asc())
				return render_template('updateMachine.html', formLogout=formLogout, form=form, data=data)

			machineTemp.nameMachine = request.form['nameMachine']
			machineTemp.descriptionMachine = request.form['descriptionMachine']
			db.session.commit() 
			flash('Maquina actualizada exitosamente', 'AC')
			return redirect(url_for('homeRoute'))
		else:
			data = db.session.query(machine.id, machine.nameMachine).order_by(machine.id.asc())
			return render_template('updateMachine.html', formLogout=formLogout, form=form, data=data)

	def viewMachineRoute(self, request):
		formLogout = loginForm()
		data = db.session.query(machine.id, machine.nameMachine).order_by(machine.id.asc())
		return render_template('viewMachine.html', formLogout=formLogout, data=data)

	def getMachineRoute(self, request):
		dataRequest = request.json
		data = db.session.query(machine).filter(machine.id == dataRequest['codeMachine']).first()
		xxx = data.__dict__
		xxx.pop('_sa_instance_state', None)
		return json.dumps(xxx)
