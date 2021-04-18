from appPackage.models import db, user, machine, component, utilization, purchase
from appPackage.formsValidation import loginForm, registerForm
from appPackage.routes import *
from flask import render_template, request, redirect, url_for, flash

class RegisterController():
	def __init__(self):
		pass
		
	def registerRoute(self, request):
		form = registerForm(request.form) # Creacion del formulario
		formLogout = loginForm()
		if request.method == 'POST' and form.validate():
			userTemp = db.session.query(user).filter(user.nameUser == request.form['nameUser']).first()
			if userTemp: # error de nombre
				flash('Error: Ya existe una cuenta registrada a ese nombre', 'WA')
				return render_template('register.html', formLogout=formLogout, form=form)
			userTemp = db.session.query(user).filter(user.username == request.form['username']).first()
			if userTemp: # error de nombre de usuario
				flash('Error: Ya existe una cuenta registrada a ese nombre de usuario', 'WA')
				return render_template('register.html', formLogout=formLogout, form=form)
			userNuevo = user(nameUser=request.form['nameUser'], username=request.form['username'], typeUser=request.form['typeUser'])
			userNuevo.set_password(request.form['password'])
			db.session.add(userNuevo)
			db.session.commit() 
			flash('Usuario registrado exitosamente', 'AC')
			return redirect(url_for('homeRoute'))
		else:
			return render_template('register.html', formLogout=formLogout, form=form)

