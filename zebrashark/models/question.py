class Question(db.Model):
    text = db.Column(db.String)
    topic = db.Column(db.String)

    def as_dict(self):
        obj = {
            'name': self.name,
            ...
        }
        return obj