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

if __name__ == "__main__":
    app.run()