from rom import Model,String

class Question(Model):
    text = String(required=True, unique=True)
    topic = String(required=True)
    stance1 = String(required=True)
    stance2 = String(required=True)


