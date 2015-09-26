from datetime import datetime
from random import randint
import flask
from zebrashark.api.login import requires_auth
from zebrashark.app import app
from zebrashark.models.conversation import Conversation, ConversationEntry, ConversationParticipant
from zebrashark.models.question import Question
from zebrashark.models.user import User
from flask import request, jsonify
from hashlib import md5

import logging
from zebrashark.models.vote import Vote

logger = logging.getLogger(__name__)

@app.route('/api/conversation', methods=['GET'])
def get_conversations():
    #return get_conversations_hardcoded()
    cs = Conversation.query.all()
    return flask.jsonify(conversations=[c.to_json() for c in cs])

def get_conversations_hardcoded():
    password = "hunter2"
    hash = md5(password).hexdigest()
    user_one = User.get_by(email_address="unicorn_hunter@gmail.com") or \
               User(email_address="unicorn_hunter@gmail.com", name="Bob", hash=hash)
    user_two = User.get_by(email_address="unicorn_saver@gmail.com") or \
               User(email_address="unicorn_saver@gmail.com", name="Jane", hash=hash)
    entries = [
        ConversationEntry(user=user_one, text="KILL ALL UNICORNS!!!1111", time=datetime.now()),
        ConversationEntry(user=user_two, text="NNNooooooooooo", time=datetime.now())
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
    return flask.jsonify({"conversations": [conversation.to_json()]}), 200


@app.route('/api/conversation/<id>/entry', methods=['POST'])
@requires_auth
def add_new_entry(id):
    message = request.get_json()
    spec_message = message['text']
    email = message['email']
    user = User.get(email)
    spec_time = datetime.now()
    conversation = Conversation.get(id)
    new_message = ConversationEntry(text=spec_message, user=user, time=spec_time)
    conversation.entries.append(new_message)
    score = randint(-8, 20)
    vote = Vote(user=user, score=score, conversation=conversation)
    conversation.votes.append(vote)
    conversation.save()
    return '', 200

@app.route('/api/conversation/<id>')
def get_conversation(id):
    conversation = Conversation.get(id)
    if conversation == None:
        return '', 404
    else:
        return jsonify(conversation.to_json)