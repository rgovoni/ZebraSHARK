#!/usr/bin/env python2
from datetime import datetime
from hashlib import md5
from flask import Flask
import redis
import os

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)
import rom.util
rom.util.CONNECTION = redis

app = Flask(__name__)

import zebrashark.api.signup
import zebrashark.api.conversation
import zebrashark.api.login

import zebrashark.views

from zebrashark.models.conversation import ConversationEntry, ConversationParticipant, Conversation
from zebrashark.models.question import Question
from zebrashark.models.user import User


def setup_hardcoded_data():
    user_one = 'demosthenes'
    user_two = 'locke'
    question = ''
    conversation = ''
    password = "hunter2"
    hash = md5(password).hexdigest()
    user_one = User(email_address="unicorn_hunter@gmail.com", name="Bob", hash=hash)
    user_two = User(email_address="unicorn_saver@gmail.com", name="Jane", hash=hash)
    user_one.save()
    user_two.save()
    logger.error("USER IDS %s %s", user_one.id, user_two.id)
    ce1 = ConversationEntry(user=user_one, text="KILL ALL UNICORNS!!!1111", time=datetime.now())
    ce2 = ConversationEntry(user=user_two, text="NNNooooooooooo", time=datetime.now())
    ce1.save()
    ce2.save()
    entries = [
        ce1,
        ce2
    ]
    participants = [
        ConversationParticipant(user=user_one, stance="KILL ALL UNICORNS"),
        ConversationParticipant(user=user_two, stance="SAVE THE UNICORNS"),
    ]
    question_text = "Should unicorn hunting be outlawed?"
    question = Question.get_by(text=question_text) or Question(text=question_text, topic="Conservation")
    conversation = Conversation(
        votes=[],
        entries=entries,
        participaints=participants,
        question=question)
    conversation.save()

#setup_hardcoded_data()

if __name__ == "__main__":
    app.run()
