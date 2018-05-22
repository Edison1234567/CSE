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
        print("%s puts on the suit" % self.name)


class Programmer(Employee):
    def __init__(self, name, age, suit, computer):
        super(Programmer, self).__init__(name, age, suit)
        self.computer = computer

    def turn_on(self):
        print("%s turns on the computer" % self.name)
