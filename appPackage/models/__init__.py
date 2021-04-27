from flask_sqlalchemy import SQLAlchemy
from appPackage import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flaskdatabase'
app.config['SECRET_KEY'] = 'random string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from appPackage.models.UserModel import user

def resetDataBase():
	db.drop_all()
	db.create_all()
	userNuevo = user(nameUser='Miguel Angel', username='admin123', typeUser='2')
	userNuevo.set_password('admin123')
	db.session.add(userNuevo)
	db.session.commit() 