#!/usr/bin/python3
'''Flask server (variable app)'''

from flask import Flask
from flask_cors import CORS
from api.v1.views import app_views
from models import storage
from os import getenv
import jsonify


app = Flask(__name__)
app.register_blueprint(app_views)
cors = Cors(app, resources={r'/api/*': {'origins': '0.0.0.0'}})


@app.teardown_appcontext
def downtear(ex):
    '''Status of your API'''
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    '''return render_template'''
    return jsonify({'error' : 'Not found'})


if __name__ == "__main__":
    if getenv('HBNB_API_HOST'):
        host = getenv('HBNB_API_HOST')
    else:
        host = '0.0.0.0'
    if getenv('HBNB_API_HOST'):
        port = getenv('HBNB_API_PORT')
    else:
        port = 5000
    app.run(host=host, port=port, debug=True)
