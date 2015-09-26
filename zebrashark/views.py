import flask

from zebrashark.app import app


@app.route("/")
def view_index():
    return app.send_static_file('index.html')

@app.route("/login")
def view_login():
    return app.send_static_file('login.html')

@app.route("/test/<value>")
def view_echo(value):
    response = {"input": value}
    return flask.jsonify(response)

@app.route("/conversation")
def view_conversation():
    return app.send_static_file('conversation.html')

@app.route("/signup")
def view_signup():
    return app.send_static_file('signup.html')

@app.route("/profile")
def view_profile():
    return app.send_static_file('profile.html')