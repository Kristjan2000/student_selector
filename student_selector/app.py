from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)


def load_students():
    with open("students.txt", "r") as file:
        students = file.readlines()
    return [student.strip() for student in students]

@app.route("/")
def index():
    students = load_students()
    if students:
        
        selected_student = random.choice(students)
    else:
        selected_student = "No students available."
    return render_template("index.html", student=selected_student)

if __name__ == "__main__":
    app.run(debug=True)

