'''This file is used to create,enter,get data from database'''
# pylint: disable= E1101, C0413, R0903, W0603, W1508
from app import DB

class Person(DB.Model):
    '''The person class is used to store and retrieve data from database'''
    username = DB.Column(DB.String(80),
                         primary_key=True,
                         unique=True,
                         nullable=False)
    score = DB.Column(DB.Integer, nullable=False)

    def __repr__(self):
        return '<Person %r>' % self.username
