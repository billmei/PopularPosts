import os
from flask import Flask
from flask.ext.assets import Environment, Bundle


app = Flask(__name__, instance_relative_config=True, static_url_path='/static')
app.config.from_object('config')
try:
    # Configuration from instance folder
    app.config.from_pyfile('config.py')
except EnvironmentError:
    pass

assets = Environment(app)

assets.load_path = [
    os.path.join(os.path.dirname(__file__), 'static/sass'),
    os.path.join(os.path.dirname(__file__), 'static/js'),
    os.path.join(os.path.dirname(__file__), 'static/bower_components'),
    os.path.join(os.path.dirname(__file__), 'static/gen'),
]

assets.register(
    'js_all',
    Bundle(
        'jquery/dist/jquery.min.js',
        'bootstrap/dist/js/bootstrap.min.js',
        'all.js',
        filters='jsmin',
        output='gen/packed.js'
    )
)
assets.register(
    'scss_all',
    Bundle(
        'bootstrap/dist/css/bootstrap.css',
        'all.scss',
        filters='pyscss,cssmin',
        output='gen/packed.css'
    )
)

from app import views