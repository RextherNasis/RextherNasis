# Student Grade Evaluation API

This project is a Flask-based REST API that evaluates student grades
and determines whether a student passed or failed.

## Features
- Input validation
- Structured JSON responses
- Professional Flask architecture
- Deployable on Render

## API Endpoint

GET /api/grade

Example Request:

/api/grade?name=Rexther&grade=85

Example Response:

{
 "success": true,
 "data": {
  "student_name": "Rexther",
  "grade": 85,
  "passing_grade": 75,
  "result": "Passed"
 }
}