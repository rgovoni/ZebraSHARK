from rom import Model,String,OneToMany

class User(Model):
    email_address = String(required=True, unique=True)
    name = String(required=True, unique=True)
    hash = String(required=True)
    conversation_entries = OneToMany('ConversationEntry','no action')
    conversations = OneToMany('ConversationParticipant')
