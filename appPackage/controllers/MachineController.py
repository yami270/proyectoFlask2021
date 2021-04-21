from appPackage.models import db, user, machine, component, utilization, purchase
from appPackage.formsValidation import loginForm, registerForm, machineForm
from appPackage.routes import *
from flask import render_template, request, redirect, url_for, flash
import json

class MachineController():
	def __init__(self):
		pass

	def registerMachineRoute(self, request):
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
