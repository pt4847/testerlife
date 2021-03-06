import logging
from logging.handlers import RotatingFileHandler
from flask import Flask , redirect
from flask_restful import Api, Resource
from flask_login import LoginManager, login_user, login_required  , logout_user , current_user
from interface import config


app = Flask(__name__)
app.config.from_object(config)
app.secret_key = '\x12my\x0bVO\xeb\xf8\x18\x15\xc5_?\x91\xd7h\x06AC'
api = Api(app)
login = LoginManager(app)
login.session_protection = "strong"
"""
    app.logger is project logging module
"""

handler = RotatingFileHandler('../logs/app.log', maxBytes=10000, backupCount=1)
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(name)s:%(lineno)d]'
))
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)


@app.route('/')
def reindex():
    return redirect('/auth/')
