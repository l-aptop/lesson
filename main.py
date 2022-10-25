class Student:
    __slots__ = ("name", "height", "hobbies", "who")
    students = []

    def __init__(self, name: str, height: int, hobbies: list = []):
        self.name = name
        self.height = height
        self.hobbies = hobbies
        self.students.append(self)
        self.who = "Student"

    def __str__(self):
        return self.name

    def __repr__(self):
        string = f"Hi! My name is {self.name} and my height is {self.height}, i am a {self.who}!\nMy hobbies are: "
        for i in self.hobbies:
            string += f"{i}, "
        return string[0:len(string)-2] if len(self.hobbies) >= 1 else string[0:len(string)-17]

    def __int__(self):
        return self.height

    def introduce(self):
        return print(repr(self))

    def grow(self, height: int = 1):
        self.height += height
        return True


class Teacher(Student):
    teachers = []
    __slots__ = ("name", "height", "hobbies", "who", "students")

    def __init__(self, name: str, height: int, hobbies: list = []):
        self.name = name
        self.height = height
        self.hobbies = hobbies
        self.teachers.append(self)
        self.who = "Teacher"
        self.students = []

    def add_student(self, this_student: Student):
        self.students.append(this_student)


me = Student(name="student", height=190, hobbies=["Programming"])
someone = Student(name="student 2", height=91)

teacher = Teacher(name="teacher", height=999)
teacher2 = Teacher(name="teacher 2", height=999, hobbies=["hobby 1", "hobby 2"])
teacher.add_student(me)
teacher2.add_student(someone)
for student in Student.students:
    student.introduce()
for teacher in Teacher.teachers:
    teacher.introduce()

for student in teacher.students:
    student.introduce()
for student in teacher2.students:
    student.introduce()
me.grow(9999)
me.introduce()
