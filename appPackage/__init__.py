from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

# Agregando el login manager
login_manager = LoginManager(app)
login_manager.login_view = 'loginRoute'
login_manager.init_app(app)

from appPackage import models
from appPackage import routes
