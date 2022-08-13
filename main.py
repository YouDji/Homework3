# 1
class Person:
    def __init__(self, age: int, name, surname):
        self.age = age
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.age}{self.name}{self.surname}"

    # 2


class Student(Person):

    def __init__(self, kurs: int, s_b: float, age: int, name, surname):
        super().__init__(age, name, surname)
        self.kurs = kurs
        self.s_b = s_b

    def __str__(self):
        return f"{self.name}{self.surname}{self.age}{self.kurs}{self.s_b}"


x = Student(2, 3.4, 18, "Dan", "Manych")
print(x.__str__())









