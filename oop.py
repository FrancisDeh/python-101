from datetime import date


class Person(object):
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        # protected variable
        self._jira = None

    def display(self):
        print(self.name)
        print(self.id_number)

    def __del__(self):  # destructor
        print("Dead")


# python does multi-inheritance - Employee(Person, Account)
class Employee(Person):
    def __init__(self, name, id_number, salary, post, credit=4):
        self.salary = salary
        self.post = post
        # private variable
        self.__credit = credit

        Person.__init__(self, name, id_number)

    def credit(self): return self.__credit * 5


# creation of an object variable or an instance
a = Employee('Jake', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()
print(a.credit())


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age): return age >= 18


student1 = Student("James", 24)
student2 = Student.from_birth_year("James", 1996)
print(student1.age, student2.age, Student.is_adult(14))
