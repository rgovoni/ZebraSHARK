import flask
from zebrashark.app import app
from functools import wraps
from flask import request, Response
import logging
from zebrashark.models.user import User
from hashlib import md5

logger = logging.getLogger(__name__)

@app.route("/api/login", methods=["POST"])
def login():
    logger.info("Got signup request: " + repr(flask.request.form))
    username = request.form['username']
    password = request.form['password']
    if check_auth(username, password):
        return '', 200
    else:
        return '', 401

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    user=User.get_by(email_address=username)
    if user == None:
        return False
    if md5(password).hexdigest() != user.hash
        return False
    return True

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
