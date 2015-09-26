from rom import Model, String, OneToMany, OneToOne


class Question(Model):
    text = String(required=True, unique=True)
    topic = String(required=True)
    stance = String(required=True)
    conversation = OneToMany('Conversation')
    stance_value = OneToOne('Stance', 'no action')


class Stance(Model):
    text = String(required=True)
    user = OneToOne('User', 'no action')
    question = OneToOne('Question', 'no action')
