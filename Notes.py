print("Hello world")
# This is a new note

# Edison Shapiro

a = 4
b = 3

print(3 + 5)
print(5 - 3)
print(3 * 5)
print(6 / 2)
print(3 ** 2)

print()
print("Try to figure out how this works")
print(13 % 5)

# the "%" sign is a modulus. It finds the remainder.

car_name = "The Edison Mobile"
car_type = "BMW"
car_cylinders = 8
car_mpg = 5000.9

print("I have a car called %s. It's pretty nice." % car_name)
print("I have a car called %s. It's a %s." % (car_name, car_type)) # watch the order

# Here is where we get a little fancy
print("What is your name?")
name = input(">_ ")
print("Hello %s." % name)

age = input("How old are you?")
print("%s?! That's really old. You belong in a retirement home." % age)

# Functions


def print_hw():
    print ("Hello World.")
    print ("Enjoy the day.")


print_hw()


def say_hi (name):# Name is a "parameter"
    print("Hello %s" % name)
    print("Coding is great!")


say_hi("Edison")


def print_age(name, age):
    print("%s is %d years old" % (name, age))
    age += 1 #age = age + 1
    print("Next year, %s will be %d years old" % (name, age))


print_age("John", 15)


def algebra_hw(x):
    return x**3 + 4*x**2 + 7 * x - 4

print(algebra_hw(3))
print(algebra_hw(4))
print(algebra_hw(5))
print(algebra_hw(6))
print(algebra_hw(7))
print(algebra_hw(8))


# if statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:  # else if
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


print(grade_calc(59))

'''Write a function called "happy_bday"
that "sings" (prints) Happy birthday
It must take one parameter called "name"
'''


def happy_bday(name):
    print("Happy Birthday to you" + ',')
    print("Happy Birthday to you" + ',')
    print("Happy Birthday dear " + name + ',')
    print("Happy Birthday to you" + ',')


happy_bday("Edison")

# Loops

for num in range(10):
    print(num + 1)

a = 1
while a < 10:
    print(a)
    a += 1

# Random Numbers
import random  # this should be on line 1
print(random.randint(0,10))


# Recasting
c = '1'
print(c == 1)   # we have a string and an int
print(int(c) == 1)
print(c == str(1))


# Comparisons

print(1 == 1)   # Use a double equal sign
print(1 != 2)   # 1 is not equal to 2
print(not False)

the_count = [1, 2, 3, 4, 5]
cheeseburger_ingredients = ['cheese', "beef", "sauce", "sesame seed buns", "avacado"]
print(cheeseburger_ingredients[3])
print(len(cheeseburger_ingredients))

# Going through lists
for generic_item_name in cheeseburger_ingredients:
    print(generic_item_name)

for item in the_count:
    print(item * 2)

length = len(cheeseburger_ingredients)
range(5) # A list of the numbers 0 through 4
range(len(cheeseburger_ingredients)) # Generate a list of all indices

for num in range(len(cheeseburger_ingredients)):
    item = cheeseburger_ingredients[num]
    print("The item at index %d is %s" % (num, item))


    #Recasting into a list
str0ne = "Hello World!"
list0ne = list(str0ne)
print(list0ne)
list0ne[11] = '.'
print(list0ne)
print(list0ne[-1])

# Adding things to a list
print(cheeseburger_ingredients.append("Fries"))
print("Fries")

#Remove things from a list
cheeseburger_ingredients.pop(1)
print(cheeseburger_ingredients)
cheeseburger_ingredients.remove("cheese")
print(cheeseburger_ingredients)

# Getting the alphabet
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)

# Making things Lowercase
strTwo = "ThIs Is A Very oDd sEnTeNCe"
lowercase = strTwo.lower()
print(lowercase)


# Dictionaries - Made up of key: value pair

dictionary = {"name": 'Lance', 'age': 26, 'height': 12 + 2}

# Accessing things from a dictionary
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

# Add a pair to a dictionary
dictionary["profession"] = "telemarketer"

large_dictionary = {
    'CA': 'California',
    'AZ': 'Arizona',
    'NY': 'New York'
}
print(large_dictionary['NY'])

larger_dictionary = {
    'CA': [
        'Fresno',
        "San Francisco",
        "San Jose"
    ],
    'NY': [
        "New York City",
        "Brooklyn",
        ]
}
print(larger_dictionary['NY'])
print(larger_dictionary['NY'][1])
print(larger_dictionary["AZ"][0])

largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
            ]

    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6936000,
        'BORDER ST': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY':{
        'NAME': "New York",
        'POPULATION':19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennslvania',
            'New Jersey'
        ]
    }
}

current_node =largest_dictionary['NY']
print(current_node['NAME'])
print(current_node['POPULATION'])