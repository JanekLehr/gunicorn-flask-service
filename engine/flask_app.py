from importlib import import_module
from flask import Flask

app = Flask(__name__)
import_module('api.routes')
