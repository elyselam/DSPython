#class Question:
#      def __init__(self, prompt, answer):
#          self.prompt = prompt
#          self.answer = answer
#
# question_prompt = ["are you butt face?", "butt?", "face?"]
# questions = [
#     Question(question_prompt[0], 'yes'),
#     Question(question_prompt[1], 'butt'),
#     Question(question_prompt[2], 'face'),
# ]
#
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(str(question.prompt))
#         if answer == question.answer:
#             score += 1
#     print("you got "+str(score) + "/" +str(len(questions)) + " correct")
# run_test(questions)

# class Student:
#     def __init__(self, name, major, gpa, is_on_probation):
#         self.name = name
#         self.major = major
#         self.gpa = gpa
#     def on_honor_roll(self):
#         if self.gpa >= 3.5:
#             return True
#         else:
#             return False
# student1 = Student("Jim", "Business", 3.1, False)
# print(student1.on_honor_roll())



class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return self.name + " is age " + str(self.age)
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] #to append with add_student()

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True #if added successfully
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value /len(self.students)

s1 = Student("Tim", 20, 95)
s2 = Student("bill",19, 75)
s3 = Student("butt", 30, 40)


course = Course("Science",2)
course.add_student(s1)
course.add_student(s2)

print(course.students) #[<__main__.Student instance at 0x10ae60758>,
print(course.students[0].name)
print(course.students.)












