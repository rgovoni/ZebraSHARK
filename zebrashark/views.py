from flask import render_template
import flask

from zebrashark.app import app


@app.route("/")
def view_index():
    return render_template('index.html')

@app.route("/login")
def view_login():
    return render_template('login.html')

@app.route("/test/<value>")
def view_echo(value):
    response = {"input": value}
    return flask.jsonify(response)

@app.route("/about")
def view_about():
    return "this is what is up"

@app.route("/conversation")
def view_conversation():
    return render_template('conversation.html')

@app.route("/signup")
def view_signup():
    return render_template('signup.html')

@app.route("/profile")
def view_profile():
    return render_template('profile.html')