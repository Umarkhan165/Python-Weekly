class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"Added grade {grade} for {self.name}")

    def average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def __str__(self):
        return f"Student: {self.name}, Average Grade: {self.average():.2f}"

s1 = Student("Umar")
s1.add_grade(90)
s1.add_grade(85)
s1.add_grade(78)
print(s1)
