class User(db.Model):
    name = db.Column(db.String(128), nullable=False)
    conversation = db.Column(db.)

    def as_dict(self):
        obj = {
            'name': self.name,
            ...
        }
        return obj