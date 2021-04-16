from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from appPackage import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flaskdatabase'
app.config['SECRET_KEY'] = 'random string'

db = SQLAlchemy(app)

class user(UserMixin, db.Model):
	id = db.Column('codeUser', db.Integer, primary_key = True)
	nameUser = db.Column(db.String(100), unique=True, nullable=False)
	username = db.Column(db.String(100), unique=True, nullable=False)
	password = db.Column(db.String(100), nullable=False)
	typeUser = db.Column(db.Integer, nullable=False)

	def set_password(self, password):
		self.password = generate_password_hash(password, method='sha256')

	def check_password(self, password):
		return check_password_hash(self.password, password)


class machine(db.Model):
	id = db.Column('codeMachine', db.Integer, primary_key = True)
	nameMachine= db.Column(db.String(100), unique=True, nullable=False)
	descriptionMachine = db.Column(db.String(255), nullable=True)
	components = db.relationship('component', backref='machine', lazy=True)

class component(db.Model):
	id = db.Column('codeComponent', db.Integer, primary_key = True)
	codeMachine = db.Column(db.Integer, db.ForeignKey('machine.codeMachine'), nullable=False)
	nameComponent = db.Column(db.String(100), unique=True, nullable=False)
	typeComponent = db.Column(db.Integer, nullable=False)
	priority = db.Column(db.Integer, nullable=False)
	notes = db.Column(db.String(255), nullable=True)
	currentStock = db.Column(db.Integer, nullable=False)
	minimumStock = db.Column(db.Integer, nullable=False)
	purchases = db.relationship('purchase', backref='component', lazy=True)
	utilizations = db.relationship('utilization', backref='component', lazy=True)

class utilization(db.Model):
	id = db.Column('utilizationId', db.Integer, primary_key = True)
	codeComponent = db.Column(db.Integer, db.ForeignKey('component.codeComponent'), nullable=False)
	date = db.Column(db.String(50), nullable=False)
	amount = db.Column(db.Integer, nullable=False)

class purchase(db.Model):
	id = db.Column('purchaseId', db.Integer, primary_key = True)
	codeComponent = db.Column(db.Integer, db.ForeignKey('component.codeComponent'), nullable=False)
	date = db.Column(db.String(50), nullable=False)
	amount = db.Column(db.Integer, nullable=False)

#db.drop_all()
#db.create_all()
