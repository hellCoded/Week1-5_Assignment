import json
import pandas as pd

FILENAME = "week5.json"
REPORT_FILE = "report.csv"

def load_students(filename=FILENAME):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ No data file found, starting fresh.")
        return []
    except json.JSONDecodeError:
        print("❌ Error: Corrupted JSON file.")
        return []

def save_students(students, filename=FILENAME):
    try:
        with open(filename, "w") as f:
            json.dump(students, f, indent=4)
        print(f"✅ Data saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving data: {e}")

def add_students():
    students = load_students()
    while True:
        name = input("Enter name (leave blank to stop): ").strip()
        if name == "":
            break
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("⚠️ Invalid age, setting age=0")
            age = 0
        course = input("Enter course: ").strip()
        student = {"name": name, "age": age, "course": course}
        students.append(student)
    save_students(students)

def generate_report(students, report_file=REPORT_FILE):
    if not students:
        print("⚠️ No student data to generate report.")
        return

    df = pd.DataFrame(students)

    avg_age = df["age"].mean() if not df.empty else 0
    course_counts = df["course"].value_counts()

    summary = pd.DataFrame({
        "Metric": ["Total Students", "Average Age"] + list(course_counts.index),
        "Value": [len(df), avg_age] + list(course_counts.values)
    })

    summary.to_csv(report_file, index=False)
    print(f"📊 Report generated → {report_file}")

def main():
    add_students()
    students = load_students()
    generate_report(students)

if __name__ == "__main__":
    main()
