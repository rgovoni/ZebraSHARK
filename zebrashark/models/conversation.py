from rom import Model, String, OneToMany, OneToOne, DateTime

class Conversation(Model):
    votes = OneToMany('Vote')
    entries = OneToMany('ConversationEntry')
    participants = OneToMany('ConversationParticipant')
    question = OneToOne('Question', 'no action')

    def to_json(self):
        return {
            "id": self.id,
            "question": self.question.to_dict(),
            "rating": self.compute_rating(),
            "users": [p.to_dict() for p in self.participants],
            "messages": [e.to_dict() for e in self.entries]
        }

    def compute_rating(self):
        return sum(v.score for v in self.votes)

class ConversationEntry(Model):
    user = OneToOne('User', 'no action')
    conversation = OneToOne('Conversation', 'no action')
    text = String(required=True)
    time = DateTime(required=True)

class ConversationParticipant(Model):
    user = OneToOne('User', 'no action')
    conversation = OneToOne('Conversation', 'no action')
    stance = String(required=True)



