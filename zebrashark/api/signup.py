from flask import request
import flask
from zebrashark.app import app
from hashlib import md5
import logging
from zebrashark.models.user import User

logger = logging.getLogger(__name__)

@app.route("/api/signup", methods=["POST"])
def signup():
    logger.info("Got signup request: " + repr(request.form))
    return '', 200

@app.route("/api/signup/form", methods=["POST"])
def getform():
    firstname = request.form['firstNameInput']
    lastname = request.form['lastNameInput']
    name = firstname + lastname
    email = request.form['usernameInput']
    pw1 = request.form['passwordInput']
    pw2 = request.form['confirmPasswordInput']
    if pw1 == pw2:
        hash = md5(pw1).hexdigest()
    user = User(email_address=email, name=name, hash=hash)
    user.save()
