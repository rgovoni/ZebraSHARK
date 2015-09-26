from rom import Model, String, OneToMany, OneToOne
from zebrashark.models.answer import Answer
from zebrashark.models.question import Stance


class User(Model):
    email_address = String(required=True, unique=True)
    name = String(required=True)
    hash = String(required=True)
    conversation_entries = OneToMany('ConversationEntry')
    conversations = OneToMany('ConversationParticipant')
    stance_value = OneToMany('Stance')
    survey_answer = OneToOne('Answer', 'no action')
