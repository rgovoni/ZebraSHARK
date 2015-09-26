#!/usr/bin/env python2

from flask import Flask
import redis
import os

import logging

logging.basicConfig(level=logging.INFO)

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)

from rom import util
util.set_connection_settings(host=redis_url, db=7)

app = Flask(__name__)

import zebrashark.api.signup
import zebrashark.api.conversation

import zebrashark.views



if __name__ == "__main__":
    app.run()
