# Added comments where needed.

# User variables.
age = int(input("Enter your age: "))
name = input("Enter your name: ")
hair_colour = input("Enter your hair colour: ")
eye_colour = input("Enter your eye colour: ")

class Adult():  # Creating adult class.
    def __init__(self, age, name, hair_colour, eye_colour):
        self.age = age
        self.name = name
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour
       
       
    def can_drive(self):  # Creating method in adult class.
        print(self.name, "is old enough to drive" )


class child(Adult):  # Creating subclass to inherit adult class features.
    def can_drive(self):  # Method in subclass.
        if age < 18:
            print(self.name, "you are too young to drive.")   

if age >= 18:  # Determines wheter user is old enough to drive or not.
    driver = Adult(age, name, hair_colour, eye_colour)
    driver.can_drive()
else:
    driver = child(age, name, hair_colour, eye_colour)
    driver.can_drive()
