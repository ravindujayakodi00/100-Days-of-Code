student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# Don't change the above code

# TODO-1: Create an empty dictionary called student grades.
student_grades = {}

# TODO-2: Write your code below to add the graded to student grades
for item in student_scores:
    score = student_scores[item]
    if 100 >= score >= 91:
        grade = "Outstanding"
    elif 90 >= score >= 81:
        grade = "Exceeds Expectation"
    elif 80 >= score >= 71:
        grade = "Acceptable"
    elif 70 >= score:
        grade = "Fail"

    student_grades[item] = grade

print(student_grades)
