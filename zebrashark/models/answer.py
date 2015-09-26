from rom import Model, OneToOne, Boolean

class Answer(Model):
    supports = Boolean(required=True)
    question = OneToOne('Question')
    user = OneToOne('User')
