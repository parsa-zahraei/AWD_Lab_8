# src/controllers/quiz_controller.py
from flask import Blueprint, request, jsonify
from src.services.quiz_service import QuizService

quiz_bp = Blueprint('quiz', __name__, url_prefix='/api/quizzes')

@quiz_bp.route('', methods=['POST'])
def create_quiz():
    # INCOMPLETE: Initialize the QuizService
    # TODO: Initialize an instance of QuizService (Hint: service = QuizService())
    service = QuizService()
    
    # INCOMPLETE: Retrieve JSON data from the request
    # TODO: Get JSON data from the request using request.json and assign it to `data`
    data = request.get_json()

    if ((data.get('title') == None) or (data.get('questions') == None)):
        return jsonify({"error": "Incorrect submission of quiz title and questions"}), 400
    
    # INCOMPLETE: Call the create_quiz method in the service
    # TODO: Use the service to create a quiz with the `data` and store the returned quiz ID in `quiz_id`
    quiz_id = service.create_quiz(data)

    # INCOMPLETE: Return a JSON response with the quiz ID and a 201 status
    # TODO: Use jsonify to create a JSON response containing `message` and `quiz_id`, with status code 201
    return jsonify({"message": "Quiz created", "quiz_id": quiz_id}), 201
    # pass  # REMOVE when implementing

@quiz_bp.route('/<int:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    # INCOMPLETE: Initialize the QuizService
    # TODO: Initialize an instance of QuizService (Hint: service = QuizService())
    service = QuizService()
    
    # INCOMPLETE: Use the service to retrieve the quiz by its ID
    # TODO: Call the `get_quiz` method with `quiz_id` and store the result in `quiz`
    quiz = service.get_quiz(quiz_id)
    
    # INCOMPLETE: Check if the quiz exists and return a JSON response
    # TODO: If `quiz` exists, return it as a JSON response with status 200. Otherwise, return an error message with status 404.
    if (quiz != None):
        return jsonify({"title": quiz.title, "questions": quiz.questions}), 200
    else:
        return jsonify({"error": "Quiz not found"}), 404
    # pass  # REMOVE when implementing

@quiz_bp.route('/<int:quiz_id>/submit', methods=['POST'])
def submit_quiz(quiz_id):
    # INCOMPLETE: Initialize the QuizService
    # TODO: Initialize an instance of QuizService (Hint: service = QuizService())
    service = QuizService()

    # INCOMPLETE: Retrieve answers from the request JSON
    # TODO: Get the answers from the request using `request.json.get('answers')` and store in `user_answers`
    user_answers = request.json.get('answers')

    if (user_answers == None):
        return jsonify({"error": "Quiz not submitted"})
    
    # INCOMPLETE: Use the service to evaluate the quiz with the provided answers
    # TODO: Call `evaluate_quiz` with `quiz_id` and `user_answers` and store the result in `score` and `message`
    score, message = service.evaluate_quiz(quiz_id, user_answers)
    
    # INCOMPLETE: Check if evaluation was successful and return the response
    # TODO: If `score` is None, return an error with status 404. Otherwise, return `score` and `message` with status 200.
    if (score == None):
        return jsonify({"error": "Could not compute score"}), 404
    else:
        return jsonify({"score": score, "message": message}), 200
    # pass  # REMOVE when implementing
