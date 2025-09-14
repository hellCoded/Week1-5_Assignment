class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old and I am studying {self.course}."

    def is_adult(self):
        try:
            return self.age >= 18
        except TypeError:
            return False

    def __str__(self):
        return f"{self.name} ({self.age}) - {self.course}"

def main():
    students = [
        {"name": "Alice", "age": 20, "course": "Computer Science"},
        {"name": "Bob", "age": 17, "course": "Mathematics"},
        {"name": "Charlie", "age": 19, "course": "Physics"},
        {"name": "Test", "age": "N/A", "course": "Unknown"}
    ]

    student_objects = [Student(**data) for data in students]

    for student in student_objects:
        print(student.introduce())
        print(f"Adult status → {student.is_adult()}")
        print("-" * 40)

if __name__ == "__main__":
    main()
