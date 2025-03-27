age = int(input("Enter your age: "))
name = input("Enter your name: ")
hair_colour = input("Enter your hair colour: ")
eye_colour = input("Enter your eye colour: ")
class Adult():
    def __init__(self, age, name, hair_colour, eye_colour):
        self.age = age
        self.name = name
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour
       
       
    def can_drive(self):
        print(self.name, "is old enough to drive" )


class child(Adult):
    def can_drive(self):   
        if age < 18:
            print(self.name, "you are too young to drive.")   

if age >= 18:
    driver = Adult(age, name, hair_colour, eye_colour)
    driver.can_drive()
else:
    driver = child(age, name, hair_colour, eye_colour)
    driver.can_drive()
