from rom import Model, OneToOne, Boolean

class Answer(Model):
    supports = Boolean(required=True)
    question = OneToOne('Question', 'no action')
    user = OneToOne('User', 'no action')
