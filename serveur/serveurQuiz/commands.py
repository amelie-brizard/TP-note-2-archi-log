from datetime import date
import click
import os
from serveurQuiz.app import db, app
from .models import Questionnaire, Question
import json

@app.cli.command()
def loaddb():
    '''Creates the tables and populates them with data.'''

    db.create_all()

    questionnaire1 = Questionnaire(id=1, name="Quiz 1")
    question1 = Question(id = 1,
                        intitule = "Question 1",
                        propositions = json.dumps(["Oui", "Non", "Coucou"]),
                        reponse = "coucou",
                        questionnaire_id = 1)

    question2 = Question(id = 2,
                        intitule = "Question 2",
                        propositions = json.dumps(["Bonjour", "Oui", "Baguette", "Heyy"]),
                        reponse = "Heyy",
                        questionnaire_id = 1)

    questionnaire2 = Questionnaire(id=2, name="Quiz 2")
    question4 = Question(id = 4,
                        intitule = "Question 1",
                        propositions = json.dumps(["Oui", "Test", "Coucou"]),
                        reponse = "Test",
                        questionnaire_id = 2)

    question5 = Question(id = 5,
                        intitule = "Question 2",
                        propositions = json.dumps(["Oui", "Hehe", "Coucou"]),
                        reponse = "Hehe",
                        questionnaire_id = 2)

    question6 = Question(id = 6,
                        intitule = "Question3",
                        propositions = json.dumps(["Oui", "Non", "Coucou"]),
                        reponse = "Non",
                        questionnaire_id = 2)

    questionnaire3 = Questionnaire(id=3, name="Quiz 3")
    question7 = Question(id = 7,
                        intitule = "Question1",
                        propositions = json.dumps(["Oui", "Baguette", "Coucou"]),
                        reponse = "Baguette",
                        questionnaire_id = 3)

    db.session.add(questionnaire1)
    db.session.add(question1)
    db.session.add(question2)

    db.session.add(questionnaire2)
    db.session.add(question4)
    db.session.add(question5)
    db.session.add(question6)

    db.session.add(questionnaire3)
    db.session.add(question7)

    db.session.commit()