from flask import jsonify, abort, make_response, request, url_for
from flask_cors import CORS, cross_origin
from .app import app, db
from .models import Question, Questionnaire

def make_public_questionnaire(questionnaire):
    new_questionnaire = {}
    for field in questionnaire:
        if field == 'id':
            new_questionnaire['url'] = url_for('get_questionnaire', id_questionnaire=questionnaire['id'], _external=True)
        else:
            new_questionnaire[field] = questionnaire[field]
    return new_questionnaire

def make_public_questionnaire_with_questions(questionnaire):
    new_questionnaire = {}
    for field in questionnaire:
        if field == 'id':
            new_questionnaire['url'] = url_for('get_questionnaire_questions', id_questionnaire=questionnaire['id'], _external=True)
        else:
            new_questionnaire[field] = questionnaire[field]
    return new_questionnaire

def make_public_question(question):
    new_question = {}
    for field in question:
        if field == 'id':
            new_question['url'] = url_for('get_question', id_questionnaire=question['id'], id_question=question['id'], _external=True)
        else:
            new_question[field] = question[field]
    return new_question

@app.route('/quiz/api/v1.0/questionnaires', methods = ['GET'])
@cross_origin()
def get_questionnaires():
    return jsonify(questionnaires=[make_public_questionnaire(questionnaire.to_json()) for questionnaire in Questionnaire.query.all()])

@app.route('/quiz/api/v1.0/questionnaires/<int:id_questionnaire>', methods = ['GET'])
@cross_origin()
def get_questionnaire(id_questionnaire):
    questionnaire = Questionnaire.query.get_or_404(id_questionnaire)
    return jsonify(questionnaire=[make_public_questionnaire_with_questions(questionnaire.to_json())])

@app.route('/quiz/api/v1.0/questionnaires/<int:id_questionnaire>/questions', methods = ['GET'])
@cross_origin()
def get_questionnaire_questions(id_questionnaire):
    questionnaire = Questionnaire.query.get_or_404(id_questionnaire)
    questions = questionnaire.questions.all()
    return jsonify({'questions': [make_public_question(question.to_json()) for question in questions]})

@app.route('/quiz/api/v1.0/questionnaires', methods = ['POST'])
@cross_origin()
def create_questionnaire():
    questionnaires = [questionnaire.to_json() for questionnaire in Questionnaire.query.all()]
    if not request.json or not 'name' in request.json:
        abort(400)
    questionnaire = Questionnaire(id=questionnaires[-1]['id'] + 1, name=request.json['name'])
    db.session.add(questionnaire)
    db.session.commit()
    return jsonify({'questionnaire': make_public_questionnaire(questionnaire.to_json())}), 201

@app.route('/quiz/api/v1.0/questionnaires/<int:id_questionnaire>/questions', methods = ['POST'])
@cross_origin()
def create_question(id_questionnaire):
    questions = [question.to_json() for question in Question.query.all()]
    if not request.json:
        abort(400)
    if not 'intitule' in request.json:
        abort(400)
    if not 'type' in request.json:
        abort(400)
    question = Question(id=questions[-1]['id'] + 1, intitule=request.json['intitule'], questionType=request.json['type'], questionnaire_id=id_questionnaire)
    db.session.add(question)
    db.session.commit()
    return jsonify({'question': make_public_question(question.to_json())}), 201

@app.route('/quiz/api/v1.0/questionnaires/<int:id_questionnaire>/questions/<int:id_question>', methods = ['GET'])
@cross_origin()
def get_question(id_questionnaire, id_question):
    question = Question.query.get_or_404(id_question, id_questionnaire)
    return jsonify({'question': [make_public_question(question.to_json())]})

@app.errorhandler(404)
@cross_origin()
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
@cross_origin()
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.route('/quiz/api/v1.0/questionnaires/<int:id_questionnaire>', methods = ['PUT'])
@cross_origin()
def update_questionnaire(id_questionnaire):
    questionnaire = Questionnaire.query.get_or_404(id_questionnaire)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) is not str:
        abort(400)
    questionnaire.name = request.json.get('name', questionnaire.name)
    db.session.commit()
    return jsonify({'questionnaire': make_public_questionnaire_with_questions(questionnaire.to_json())})

@app.route('/quiz/api/v1.0/questionnaires/<int:id_questionnaire>/questions/<int:id_question>', methods = ['PUT'])
@cross_origin()
def update_question(id_questionnaire, id_question):
    question = Question.query.get_or_404(id_question, id_questionnaire)
    if not request.json:
        abort(400)
    if 'intitule' in request.json and type(request.json['intitule']) is not str:
        abort(400)
    if 'type' in request.json and type(request.json['type']) is not str:
        abort(400)
    question.intitule = request.json.get('intitule', question.intitule)
    question.questionType = request.json.get('type', question.questionType)
    db.session.commit()
    return jsonify({'question': make_public_question(question.to_json())})

@app.route('/quiz/api/v1.0/questionnaires/<int:id_questionnaire>', methods=['DELETE'])
@cross_origin()
def remove_questionnaire(id_questionnaire):
    questionnaire = make_public_questionnaire_with_questions(Questionnaire.query.get_or_404(id_questionnaire).to_json())
    Questionnaire.query.filter(Questionnaire.id == id_questionnaire).delete()
    db.session.commit()
    return jsonify({'questionnaire': questionnaire}), 200

@app.route('/quiz/api/v1.0/questionnaires/<int:id_questionnaire>/questions/<int:id_question>', methods=['DELETE'])
@cross_origin()
def remove_question(id_questionnaire, id_question):
    question = make_public_question(Question.query.get_or_404(id_question, id_questionnaire).to_json())
    Question.query.filter(Question.id == id_question and Question.questionnaire_id == id_questionnaire).delete()
    db.session.commit()
    return jsonify({'question': question}), 200
