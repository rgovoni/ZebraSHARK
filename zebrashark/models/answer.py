class Answer(db.Model):
    response = db.Column(db.Integer)
    text = db.Column(db.String)

    def as_dict(self):
        obj = {
            'response': self.response,
            'text': self.text,
            ...
        }
        return obj
