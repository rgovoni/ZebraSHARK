class Converation(db.Model):
    votes = db.Column(db.Integer)
    text = db.Column(db.String)
    stance = db.Column(db.String)
    topic = db.Column(db.String)

    def as_dict(self):
        obj = {
            'name': self.name,
            'text': self.text,
            'stance': self.stance,
            'topic': self.topic,
            ...
        }
        return obj
