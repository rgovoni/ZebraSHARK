from rom import Model,String,OneToMany,OneToOne,DateTime

class Conversation(Model):
    votes = OneToMany('Vote')
    entries = OneToMany('ConversationEntry')
    topic = String(required=True)
    participants = OneToMany('ConversationParticipant')

class ConversationEntry(Model):
    user = OneToOne('User','no action')
    text = String(required=True)
    time = DateTime(required=True)

class ConversationParticipant(Model):
    user = OneToOne('User','no action')
    stance = String(required=True)



