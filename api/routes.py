from __future__ import unicode_literals
from engine.flask_app import app


@app.route('/', methods=['GET'])
def hello():
    return "Hello world!\n"
