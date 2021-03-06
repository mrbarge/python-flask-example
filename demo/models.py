from dataclasses import dataclass

from . import db


@dataclass
class Thing(db.Model):
    __tablename__ = 'things'
    id: int
    thing: str
    rating: int

    id = db.Column(db.Integer, primary_key=True)
    thing = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer)

    def __init__(self, thing, rating):
        self.thing = thing
        self.rating = rating

    def __repr__(self):
        return '<id {}>'.format(self.id)
