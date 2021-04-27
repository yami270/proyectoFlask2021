from appPackage.models import db

class machine(db.Model):
	id = db.Column('codeMachine', db.Integer, primary_key = True)
	nameMachine= db.Column(db.String(100), unique=True, nullable=False)
	descriptionMachine = db.Column(db.String(255), nullable=True)
	components = db.relationship('component', backref='machine', lazy=True)