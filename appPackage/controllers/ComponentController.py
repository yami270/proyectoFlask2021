from appPackage.models import db, user, machine, component, utilization, purchase
from appPackage.formsValidation import loginForm, registerForm, machineForm, componentForm, componentUpdateForm
from appPackage.routes.routes import *
from flask import render_template, request, redirect, url_for, flash
import json

class ComponentController():
	def __init__(self):
		pass

	def registerComponentRoute(self, request):
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