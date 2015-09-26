#!/usr/bin/env python2

from flask import Flask
import redis
import os

app = Flask(__name__)

import zebrashark.api.signup

import zebrashark.views

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)

if __name__ == "__main__":
    app.run()
