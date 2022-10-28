import time
import random
import os
to_continue = lambda: input("Press enter to continue...\n> ")
clear = lambda: os.system("cls")


class InvalidArgument(Exception):
    ...


class NotHungry(Exception):
    ...


class NotEnough(Exception):
    ...


class Hungry(Exception):
    ...


class Intelligent(Exception):
    ...


class Pet:
    __slots__ = ("name", "who")

    def __init__(self, name: str):
        self.name = name
        self.who = "Pet"

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Cat(Pet):
    def __init__(self, name: str):
        self.name = name
        self.who = "Cat"


class Dog(Pet):
    def __init__(self, name: str):
        self.name = name
        self.who = "Dog"


def do_at_end(self, lose = True):
    if self.hunger > 100:
        self.hunger = 100
    elif self.hunger < 1:
        self.hunger = 1
    if lose == True:
        self.intelligence -= 1
    if self.intelligence > 100:
        self.intelligence = 100
    elif self.intelligence < 1:
        self.intelligence = 1


class Student:
    __slots__ = ("name", "height", "hobbies", "who", "money", "hunger", "intelligence", "work_allowed", "learn_allowed", "teacher", "pet")
    students = []

    def __init__(self, name: str, height: int, hobbies: list = (), money: int = 100, teacher = None, pet = None):
        self.name = name
        self.height = height
        self.hobbies = hobbies
        self.students.append(self)
        self.who = "Student"
        self.money = money
        self.hunger = 100
        self.intelligence = 1
        self.work_allowed = 10
        self.learn_allowed = 6
        self.teacher = teacher
        self.pet = pet

    def __str__(self):
        return self.name

    def __repr__(self):
        NEWLINE = "\n"
        string = f"Hi! My name is {self.name} and my height is {self.height}, i am a {self.who}!\nMy hobbies are: "
        for i in self.hobbies:
            string += f"{i}, "
        v1 = string[0:len(string)-2] if len(self.hobbies) >= 1 else string[0:len(string)-17]
        v2 = v1 + f"{NEWLINE+'My teacher is ' + self.teacher.name if self.teacher != None else ''}{NEWLINE + 'My pet is a ' + self.pet.who + ' named ' + self.pet.name if self.pet != None else ''}"
        return v2

    def __int__(self):
        return self.height

    def introduce(self):
        return print(repr(self))

    def work(self, work_time: int = 1):
        if work_time < 1 or work_time > self.work_allowed:
            raise InvalidArgument(f"You can not work for more than {self.work_allowed} hours or less than 1 hour as a {self.who}")
        removed = round(work_time*5/(self.intelligence/1.5))
        if self.hunger < removed:
            raise Hungry("You are hungry. Choose less work time or eat")
        added = round(random.randint(250, 500)*work_time*self.intelligence/100)
        print(f"{self.who} {self.name} is currently working (please wait for {work_time} second(s))")
        time.sleep(work_time)
        self.money += added
        self.hunger -= removed
        do_at_end(self)
        return added, removed

    def eat(self):
        if self.hunger == 100:
            raise NotHungry("You are already at max hunger")
        if self.money < 99:
            raise NotEnough("You need at least 100 money to eat")
        added = random.randint(10, 50)
        removed = 100
        self.money -= removed
        self.hunger += added
        do_at_end(self)
        return added, removed

    def learn(self, learn_time: int):
        if learn_time < 1 or learn_time > self.learn_allowed:
            raise InvalidArgument(f"You can not learn for more than {self.learn_allowed} hours or less than 1 hour as a {self.who}")
        if self.intelligence == 100:
            raise Intelligent("You are already smart enough")
        removed = round(learn_time*1.5)
        if self.hunger < removed:
            raise Hungry("You are hungry. Choose less learn time or eat")
        print(f"{self.who} {self.name} is currently learning (please wait for {learn_time} second(s))")
        time.sleep(learn_time)
        added = learn_time
        self.hunger -= removed
        self.intelligence += added
        do_at_end(self, lose=False)
        return added, removed


class Teacher(Student):
    teachers = []
    __slots__ = ("name", "height", "hobbies", "who", "money", "hunger", "intelligence", "work_allowed", "learn_allowed", "pet", "teacher", "students")

    def __init__(self, name: str, height: int, hobbies: list = (), money: int = 100, pet = None):
        self.name = name
        self.height = height
        self.hobbies = hobbies
        self.teachers.append(self)
        self.who = "Teacher"
        self.money = money
        self.hunger = 100
        self.intelligence = 1
        self.work_allowed = 10
        self.learn_allowed = 6
        self.pet = pet
        self.teacher = None
        self.students = []

    def add_student(self, this_student: Student):
        self.students.append(this_student)
        this_student.teacher = self


me = Student(name=os.getlogin(), height=190, hobbies=["Programming"], pet=Cat(name="Cat"))

my_teacher = Teacher(name="Teacher", height=187)

my_teacher.add_student(me)
os.system(f"title Student Game && cls")
me.introduce()

while True:
    print("""
    1: Work
    2: Learn
    3: Eat
    4: View your profile
    5: Exit
    """)
    print("What would you like to do?")
    action = input("> ")
    if action == "1":
        clear()
        amount = 0
        while True:
            amount = int(input(f"How many hours would you like to work for? (1 to {me.work_allowed} or 0 to cancel)\n> "))
            if amount == 0:
                clear()
                break
            if 1 < amount < me.work_allowed+1:
                break
            print(f"Please enter a number between 1 and {me.work_allowed}")
            to_continue()
            clear()
        if amount != 0:
            try:
                clear()
                worked = me.work(amount)
                clear()
                print(f"You worked for {amount} hours.\nYou got {worked[0]} money!\nYou lost {worked[1]} hunger!\n\nYou now have:\n{me.money} money\n{me.hunger} hunger")
                to_continue()
                clear()
            except Exception as e:
                print(str(e))
                to_continue()
                clear()
    if action == "2":
        clear()
        amount = 0
        while True:
            amount = int(input(f"How many hours would you like to learn for? (1 to {me.learn_allowed} or 0 to cancel)\n> "))
            if amount == 0:
                clear()
                break
            if 1 < amount < me.learn_allowed + 1:
                break
            print(f"Please enter a number between 1 and {me.learn_allowed}")
            to_continue()
            clear()
        if amount != 0:
            try:
                clear()
                worked = me.learn(amount)
                clear()
                print(f"You learned for {amount} hours.\nYou got {worked[0]} intelligence!\nYou lost {worked[1]} hunger!\n\nYou now have:\n{me.intelligence} intelligence\n{me.hunger} hunger")
                to_continue()
                clear()
            except Exception as e:
                print(str(e))
                to_continue()
                clear()
    if action == "3":
        clear()
        try:
            worked = me.eat()
            clear()
            print(f"You ate some food.\nYou got {worked[0]} hunger!\nYou lost {worked[1]} money!\n\nYou now have:\n{me.hunger} hunger\n{me.money} money")
            to_continue()
            clear()
        except Exception as e:
            print(str(e))
            to_continue()
            clear()
    if action == "4":
        clear()
        print(f"""
    > Name: {me.name}
    > Height: {me.height}
    > Role: {me.who}
    > Money: {me.money}
    > Hunger: {me.hunger}
    > Intelligence: {me.intelligence}
    > Teacher: {me.teacher.name}
    > Pet: {me.pet.name} ({me.pet.who})
""")
        to_continue()
        clear()
    if action == "5":
        exit()
