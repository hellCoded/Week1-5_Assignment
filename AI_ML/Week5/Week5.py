import json
import pandas as pd
def load_students(filename="week5.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_students(students, filename="week5.json"):
    with open(filename, "w") as f:
        json.dump(students, f, indent=4)

def add_students():
    students = load_students()
    while True:
        name = input("Enter name: ")
        if name == "":
            break
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        student = {"name": name, "age": age, "course": course}
        students.append(student)
    save_students(students)

if __name__ == "__main__":
    add_students()

    students = load_students()
    df = pd.DataFrame(students)

    avg_age = df['age'].mean() if not df.empty else 0
    course_counts = df['course'].value_counts()

summary = pd.DataFrame({
    "Metric": ["Average Age"] + list(course_counts.index),
    "Value": [avg_age] + list(course_counts.values)
})

summary.to_csv("report.csv", index=False)
