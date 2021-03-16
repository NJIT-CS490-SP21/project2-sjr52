from app import DB


class Person(DB.Model):
    username = DB.Column(DB.String(80),
                         primary_key=True,
                         unique=True,
                         nullable=False)
    score = DB.Column(DB.Integer, nullable=False)

    def __repr__(self):
        return '<Person %r>' % self.username
