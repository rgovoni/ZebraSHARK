import flask
from zebrashark.app import app

import logging

logger = logging.getLogger(__name__)

@app.route("/api/signup", methods=["POST"])
def signup():
    logger.info("Got signup request: " + repr(flask.request.form))
    return '', 200

@app.route("/api/signup/form", methods=["POST"])
def getform():
    firstname = request.form['firstNameInput']
    lastname = request.form['lastNameInput']
    username = request.form['usernameInput']
    pw1 = request.form['passwordInput']
    pw2 = request.form['confirmPasswordInput']
    if pw1 == pw2:
        hash = md5(pw1).hexdigest()

    
