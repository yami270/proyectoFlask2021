from appPackage import app

@app.route('/')
def index():
	return 'esta es la raiz'

@app.route('/login')
def loginRoute():
	return 'esto es el login'

@app.route('/home')
def homeRoute():
	return 'este es el home'

@app.route('/registroMaquina')
def registerMachineRoute():
	return 'registrar maquina'

@app.route('/registroComponente')
def registerComponentRoute():
	return 'registrar componente'

@app.route('/actualizar')
def updateRoute():
	return 'actualizar datos'

@app.route('/stock')
def stockRoute():
	return 'registrar stock'