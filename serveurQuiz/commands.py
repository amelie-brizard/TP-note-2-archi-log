from datetime import date
import click
import os
from todo.app import db, app
from .models import Questionnaire, Question

@app.cli.command()
def loaddb():
    '''Creates the tables and populates them with data.'''

    db.create_all()

    questionnaire1 = Questionnaire(id=1, name="Premier questionnaire")
    question1 = Question(id = 1,
                        title = "Question1",
                        questionType = "text",
                        questionnaire_id = 1)

    question2 = Question(id = 2,
                        title = "Question2",
                        questionType = "text",
                        questionnaire_id = 1)

    question3 = Question(id = 3,
                        title = "Question3",
                        questionType = "text",
                        questionnaire_id = 1)

    questionnaire2 = Questionnaire(id=2, name="Deuxième questionnaire")
    question4 = Question(id = 4,
                        title = "Question1",
                        questionType = "text",
                        questionnaire_id = 2)

    question5 = Question(id = 5,
                        title = "Question2",
                        questionType = "text",
                        questionnaire_id = 2)

    question6 = Question(id = 6,
                        title = "Question3",
                        questionType = "text",
                        questionnaire_id = 2)

    questionnaire3 = Questionnaire(id=3, name="Troisième questionnaire")
    question7 = Question(id = 7,
                        title = "Question1",
                        questionType = "text",
                        questionnaire_id = 3)

    question8 = Question(id = 8,
                        title = "Question2",
                        questionType = "text",
                        questionnaire_id = 3)

    question9 = Question(id = 9,
                        title = "Question3",
                        questionType = "text",
                        questionnaire_id = 3)

    db.session.add(questionnaire1)
    db.session.add(question1)
    db.session.add(question2)
    db.session.add(question3)

    db.session.add(questionnaire2)
    db.session.add(question4)
    db.session.add(question5)
    db.session.add(question6)

    db.session.add(questionnaire3)
    db.session.add(question7)
    db.session.add(question8)
    db.session.add(question9)

    db.session.commit()