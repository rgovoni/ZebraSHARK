import flask
from zebrashark.app import app
from functools import wraps
from flask import request, Response
import logging

logger = logging.getLogger(__name__)

@app.route("/api/login", methods=["POST"])
def login():
    logger.info("Got signup request: " + repr(flask.request.form))
    return '', 200

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    username = request.form['username']
    password = request.form['password']
    return username == 'admin' and password == 'secret'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
