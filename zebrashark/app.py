from flask import Flask
import flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "sugar"
@app.route("/test/<value>")
def echo(value):
    response = {"input": value}
    return flask.jsonify(response)

@app.route("/index")
def index():
    return flask.render_template('index.html')

if __name__ == "__main__":
    app.run()