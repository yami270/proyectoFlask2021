from flask import Flask

app = Flask(__name__)

from appPackage import models
from appPackage import routes