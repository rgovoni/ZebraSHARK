import flask
from zebrashark.app import app

import logging

logger = logging.getLogger(__name__)

@app.route("/api/signup", methods=["POST"])
def signup():
    logger.info("Got signup request: " + repr(flask.request.form))
    return '', 200