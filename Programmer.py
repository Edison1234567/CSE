class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, suit):
        super(Employee, self).__init__(name, age)
        self.suit = suit

    def put_on(self):
        print("You put on the suit")


class Programmer(Employee):
    def __init__(self):
        super(Programmer, self).__init__()