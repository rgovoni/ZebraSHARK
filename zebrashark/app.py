#!/usr/bin/env python2

from flask import Flask
import redis
import os

from urlparse import urlparse

import logging

logging.basicConfig(level=logging.INFO)

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)

import rom.util

rom.util.CONNECTION = redis

app = Flask(__name__)

import zebrashark.api.signup
import zebrashark.api.conversation
import zebrashark.api.login

import zebrashark.views


def setup_hardcoded_data():
    user_one = 'demosthenes'
    user_two = 'locke'
    question = ''
    conversation = ''


if __name__ == "__main__":
    setup_hardcoded_data()
    app.run()
