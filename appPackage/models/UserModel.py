from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from appPackage.models import db

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
