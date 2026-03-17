from flask import Blueprint, request, jsonify
from datetime import datetime
from .utils import evaluate_student_grade

api_routes = Blueprint("api_routes", __name__)

@api_routes.route("/")
def home():

    return jsonify({
        "message": "Student Grade Evaluation API",
        "version": "1.0",
        "endpoints": {
            "/api/grade": "Evaluate student grade"
        }
    })


@api_routes.route("/api/grade", methods=["GET"])
def check_grade():

    name = request.args.get("name")
    grade = request.args.get("grade")

    if not name or not grade:
        return jsonify({
            "success": False,
            "error": "Missing parameters (name, grade)",
            "timestamp": datetime.utcnow()
        }), 400

    try:
        grade = float(grade)
    except ValueError:
        return jsonify({
            "success": False,
            "error": "Grade must be numeric",
            "timestamp": datetime.utcnow()
        }), 400

    result = evaluate_student_grade(name, grade)

    return jsonify({
        "success": True,
        "timestamp": datetime.utcnow(),
        "data": result
    })