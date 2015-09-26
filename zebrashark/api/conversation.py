from datetime import datetime
import flask
from zebrashark.app import app
from zebrashark.models.conversation import Conversation, ConversationEntry, ConversationParticipant
from zebrashark.models.question import Question
from zebrashark.models.user import User

from hashlib import md5

@app.route('/api/conversation', methods=['GET'])
def get_conversations():
    password = "hunter2"
    hash = md5(password).hexdigest()
    user_one = User.get_by(email_address="unicorn_hunter@gmail.com") or\
               User(email_address="unicorn_hunter@gmail.com", name="Bob", hash=hash)

    user_two = User.get_by(email_address="unicorn_saver@gmail.com") or\
               User(email_address="unicorn_saver@gmail.com", name="Jane", hash=hash)
    entries = [
        ConversationEntry(user=user_one, text="KILL ALL UNICORNS!!!1111", time=datetime.now()),
        ConversationEntry(user=user_two, text="NNNooooooooooo", time=datetime.now())
    ]
    participants = [
        ConversationParticipant(user=user_one, stance="KILL ALL UNICORNS"),
        ConversationParticipant(user=user_two, stance="SAVE THE UNICORNS"),
                    ]
    question = Question(text="Should unicorn hunting be outlawed?", topic="Conservation")
    conversation = Conversation(
        votes=[],
        entries=entries,
        participaints=participants,
        question=question)
    
    return flask.jsonify([conversation.to_dict()]), 200