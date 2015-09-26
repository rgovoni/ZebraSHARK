from rom import Model, String, OneToMany, OneToOne, DateTime

class Conversation(Model):
    votes = OneToMany('Vote')
    entries = OneToMany('ConversationEntry')
    participants = OneToMany('ConversationParticipant')
    question = OneToOne('Question', 'no action')

class ConversationEntry(Model):
    user = OneToOne('User', 'no action')
    text = String(required=True)
    time = DateTime(required=True)

class ConversationParticipant(Model):
    user = OneToOne('User', 'no action')
    stance = String(required=True)



