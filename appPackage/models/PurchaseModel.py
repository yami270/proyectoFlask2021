from appPackage.models import db

class purchase(db.Model):
	id = db.Column('purchaseId', db.Integer, primary_key = True)
	codeComponent = db.Column(db.Integer, db.ForeignKey('component.codeComponent'), nullable=False)
	date = db.Column(db.String(50), nullable=False)
	amount = db.Column(db.Integer, nullable=False)
