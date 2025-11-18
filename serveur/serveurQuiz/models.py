from .app import db
from flask import url_for
from sqlalchemy import func, ARRAY

class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Questionnaire (%d) %s>" % (self.id, self.name)

    def to_json(self):
        json = {
            'id': self.id,
            'name': self.name,
        }
        return json

class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    intitule = db.Column(db.String(120))
    propositions = db.Column(db.Text)
    reponse = db.Column(db.String(120))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    questionnaire = db.relationship("Questionnaire", backref = db.backref("questions", lazy="dynamic"))

    def to_json(self):
        json = {
            'id': self.id,
            'intitule': self.intitule,
            'propositions': self.propositions,
            'reponse': self.reponse
        }
        return json
