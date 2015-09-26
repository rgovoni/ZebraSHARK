from rom import Model, Integer, OneToOne

class Vote(Model):
    user = OneToOne('User', 'no action', required=True)
    score = Integer(required=True)
    conversation = OneToOne('Conversation', 'no action', required=True)
    unique_together = [
        ('user', 'conversation'),
    ]
