from appPackage.models import db

class utilization(db.Model):
	id = db.Column('utilizationId', db.Integer, primary_key = True)
	codeComponent = db.Column(db.Integer, db.ForeignKey('component.codeComponent'), nullable=False)
	date = db.Column(db.String(50), nullable=False)
	amount = db.Column(db.Integer, nullable=False)
