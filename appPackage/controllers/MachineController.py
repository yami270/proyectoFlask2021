from appPackage.models import db, user, machine, component, utilization, purchase
from appPackage.formsValidation import loginForm, registerForm, machineForm
from appPackage.routes import *
from flask import render_template, request, redirect, url_for, flash

class MachineController():
	def __init__(self):
		pass

	def registerMachineRoute(self, request):
		form = machineForm(request.form) # Creacion del formulario
		formLogout = loginForm()
		if request.method == 'POST' and form.validate():
			machineTemp = db.session.query(machine).filter(machine.nameMachine == request.form['nameMachine']).first()
			if machineTemp: # error de nombre
				flash('Error: Ya existe una maquina registra a ese nombre', 'WA')
				return render_template('registerMachine.html', formLogout=formLogout, form=form)
			
			machineNuevo = machine(nameMachine=request.form['nameMachine'], descriptionMachine=request.form['descriptionMachine'])
			db.session.add(machineNuevo)
			db.session.commit() 
			flash('Maquina registrada exitosamente', 'AC')
			return redirect(url_for('homeRoute'))
		else:
			return render_template('registerMachine.html', formLogout=formLogout, form=form)
