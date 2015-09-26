class Vote(db.Model):
    user = db.Column(db.String(128), nullable=False)
    value = db.Column(db.Integer)

    def as_dict(self):
        obj = {
            'value': self.value,
            'user': self.user,
            ...
        }
        return obj