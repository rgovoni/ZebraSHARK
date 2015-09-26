from rom import Model, String, OneToMany, OneToOne

class User(Model):
    email_address = String(required=True, unique=True)
    name = String(required=True, unique=True)
    hash = String(required=True)
    conversation_entries = OneToMany('ConversationEntry', 'no action')
    conversations = OneToMany('ConversationParticipant')
    stance_value = OneToMany('Stance')
    survey_answer = OneToOne('Answer')
