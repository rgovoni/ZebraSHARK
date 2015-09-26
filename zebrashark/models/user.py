from rom import Model, String, OneToMany, OneToOne
from zebrashark.gravatar import gravatar_url
from zebrashark.models.answer import Answer
from zebrashark.models.question import Stance
from zebrashark.models.vote import Vote



class User(Model):
    email_address = String(required=True, unique=True)
    name = String(required=True)
    hash = String(required=True)
    conversation_entries = OneToMany('ConversationEntry')
    conversations = OneToMany('ConversationParticipant')
    stance_value = OneToMany('Stance')
    survey_answer = OneToOne('Answer', 'no action')

    def to_json(self):
        return {
            "email": self.email_address,
            "name": self.name,
            "id": self.id,
            "avatar_url": gravatar_url(self.email_address)
        }