
# Function to caclculate sum if its addition.
def addition(num1, num2):  # Takes the numbers as arguments.
    add = num1 + num2  # Calculates num1 & 2.
    if num2 == 0:  # If 0 is entered into num2 it will run the code below.
        add = num1
    add_answer = print(num1, " + ", num2, " = ", add)  
    return add_answer  # Return the sum outcome.


# Function to caclculate sum if its sub.
def subtraction(num1, num2):  # Takes the numbers as arguments.
    sub = num1 - num2  # Calculates num1 & 2.
    if num2 == 0:  # If 0 is entered into num2 it will run the code below.
        sub = num1
    sub_answer = print(num1, " - ", num2, " = ", sub)
    return sub_answer  # Return the sum outcome.
  


# Function to caclculate sum if its division.
def division(num1, num2):  # Takes the numbers as arguments.
    try:
        divide = num1 / num2  # Calculates num1 & 2.
        div_answer = print(num1, " % ", num2, " = ", divide)
    except:
        ZeroDivisionError
        divide = num1
        div_answer = print(num1, " % ", num2, " = ", divide)
        print("Cannot divide by 0.")
    return div_answer  # Return the sum outcome.


# Function to caclculate sum if its multiplication.
def multiplication(num1, num2):  # Takes the numbers as arguments.
    multiply = num1 * num2  # Calculates num1 & 2.
    if num2 == 0:  # If 0 is entered into num2 it will run the code below.
        multiply = num1  # The outcome will be just num1.
    multiply_answer = print(num1, " * ", num2, " = ", multiply)
    return multiply_answer  # Return the sum outcome.


# Create a while loop to always get an input.
while True:
    # Open the file to write the answers to.
    with open("equations.txt", "a+") as efile_open:
        num1 = ""
    # Receive integer input.
    while num1 != int():
        try:
            num1 = int(input("Number 1: "))
        except ValueError or TypeError:
            print("Please enter a valid number")
            continue
        else:
            break


    # Get input and find out the equation type.
    print(" 1. + \n 2. - \n 3. * \n 4. %")
    equation_type = ""
    options = [1, 2, 3, 4]
    while equation_type not in options:
        equation_type = int(input("Enter a valid option number please: "))
     
    num2 = ""
    # Get 2nd input.
    while num2 != int():
        try:
            num2 = int(input("Number 2: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        else:
            break


    # Calculate the equation and print it.
    if equation_type == 1:
        next_calc = input("1. Another calculation\n2. Print previous calculation\nEnter here: ")
        if next_calc == "1":
            continue
        elif next_calc == "2":
            with open("equations.txt", "a+") as efile_open:
                efile_open.write(str(addition(num1, num2)))
                break
            
        
    elif equation_type == 2:
        next_calc = input("1. Another calculation\n2. Print previous calculation\nEnter here: ")
        if next_calc == "1":
            continue
        elif next_calc == "2":
            with open("equations.txt", "a+") as efile_open:
                efile_open.write(str(subtraction(num1, num2)))
                break
        
       
    elif equation_type == 3:
        next_calc = input("1. Another calculation\n2. Print previous calculation\nEnter here: ")
        if next_calc == "1":
            continue
        elif next_calc == "2":
            with open("equations.txt", "a+") as efile_open:
                efile_open.write(str(multiplication(num1, num2)))
                break
        
    elif equation_type == 4:
        next_calc = input("1. Another calculation\n2. Print previous calculation\nEnter here: ")
        if next_calc == "1":
            continue
        elif next_calc == "2":
            with open("equations.txt", "a+") as efile_open:
                efile_open.write(str(division(num1, num2)))
                break
        
    elif equation_type == 4 and num2 == 0:
        next_calc = input("1. Another calculation\n2. Print previous calculation\nEnter here: ")
        if next_calc == "1":
            continue
        elif next_calc == "2":
            with open("equations.txt", "a+") as efile_open:
                efile_open.write(str(division(num1, num2)))
                break
    else:
        print("Not a valid sum.")
    