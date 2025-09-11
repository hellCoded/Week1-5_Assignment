class Student:
     def __init__(self ,name,age,course):
          self.name = name
          self.age = age
          self.course = course
     
     def introduce(self):
          print(f"Hello, my name is {self.name}, I am {self.age} years old and I am studying {self.course}.")

     def is_adult(self):
          return self.age >= 18

# Example usage:
students = [ {"name": "Alice", "age": 20, "course": "Computer Science"},
             {"name": "Bob", "age": 17, "course": "Mathematics"},
             {"name": "Charlie", "age": 19, "course": "Physics"}
          ]

student_objects = [Student(**data) for data in students]
for student in student_objects:
     student.introduce()
     print("Is adult:", student.is_adult())


