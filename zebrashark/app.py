#!/usr/bin/env python2

from flask import Flask
import redis
import os

from urlparse import urlparse

import logging

logging.basicConfig(level=logging.INFO)

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)

from rom import util

redis_server = urlparse(redis_url)
redis_host = redis_server.hostname
redis_port = redis_server.port
util.set_connection_settings(host=redis_host, port=redis_port, db=0)

app = Flask(__name__)

import zebrashark.api.signup
import zebrashark.api.conversation

import zebrashark.views



if __name__ == "__main__":
    app.run()
