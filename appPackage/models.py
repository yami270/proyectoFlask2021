from flask_sqlalchemy import SQLAlchemy
from appPackage import app

app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flaskdatabase'

db = SQLAlchemy(app)

class user(db.Model):
   codeUser = db.Column(db.Integer, primary_key = True)
   nameUser = db.Column(db.String(100), unique=True, nullable=False)
   username = db.Column(db.String(100), unique=True, nullable=False)
   password = db.Column(db.String(100), nullable=False)
   typeUser = db.Column(db.Integer, nullable=False)

class machine(db.Model):
   codeMachine = db.Column(db.Integer, primary_key = True)
   nameMachine= db.Column(db.String(100), unique=True, nullable=False)
   descriptionMachine = db.Column(db.String(255), nullable=True)
   components = db.relationship('component', backref='machine', lazy=True)

class component(db.Model):
   codeComponent = db.Column(db.Integer, primary_key = True)
   codeMachine = db.Column(db.Integer, db.ForeignKey('machine.codeMachine'), nullable=False)
   nameComponent = db.Column(db.String(100), unique=True, nullable=False)
   typeComponent = db.Column(db.Integer, nullable=False)
   priority = db.Column(db.String(255), nullable=False)
   notes = db.Column(db.String(255), nullable=False)
   currentStock = db.Column(db.Integer, nullable=False)
   minimumStock = db.Column(db.Integer, nullable=False)
   purchases = db.relationship('purchase', backref='component', lazy=True)
   utilizations = db.relationship('utilization', backref='component', lazy=True)

class utilization(db.Model):
   utilizationId = db.Column(db.Integer, primary_key = True)
   codeComponent = db.Column(db.Integer, db.ForeignKey('component.codeComponent'), nullable=False)
   date = db.Column(db.String(50), nullable=False)
   amount = db.Column(db.Integer, nullable=False)

class purchase(db.Model):
   purchaseId = db.Column(db.Integer, primary_key = True)
   codeComponent = db.Column(db.Integer, db.ForeignKey('component.codeComponent'), nullable=False)
   date = db.Column(db.String(50), nullable=False)
   amount = db.Column(db.Integer, nullable=False)

db.drop_all()
db.create_all()
