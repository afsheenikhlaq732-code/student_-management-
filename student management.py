class Student:
    def __init__(self, name, age, quiz_marks, assignment_marks, course):
        self.name = name
        self.age = age
        self.quiz = quiz_marks
        self.assignment = assignment_marks
        self.course = course

    def display(self):
        print("name:", self.name)
        print("age:", self.age)
        print("quiz:", self.quiz)
        print("assignment:", self.assignment)
        print("course:", self.course)

s1 = Student("burak", 23, 30, 15, "AI")
s2 = Student("sara", 23, 35, 17, "AI")
s1.display()
s2.display()