from appPackage.models import db

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