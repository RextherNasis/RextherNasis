PASSING_GRADE = 75

def evaluate_student_grade(name, grade):

    if grade >= PASSING_GRADE:
        status = "Passed"
    else:
        status = "Failed"

    return {
        "student_name": name,
        "grade": grade,
        "passing_grade": PASSING_GRADE,
        "result": status
    }