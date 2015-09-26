from flask import Flask, render_template
import flask

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test/<value>")
def echo(value):
    response = {"input": value}
    return flask.jsonify(response)

@app.route("/about")
def about():
    return "this is what is up"

@app.route("/conversation")
def conversation():
    return render_template('conversation.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run()