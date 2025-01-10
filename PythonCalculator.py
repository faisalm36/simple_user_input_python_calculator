def add(x,y):
    return x + y

    # add function that takes 
    # 2 arguments which are x & y 
    # then add both x & y and then returns the result
    # we will be able to call upon this function later in the code 
    # to perform addition
    

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x,y):
    if y == 0:
        return "ERROR: CANNOT DIVIDE BY ZERO"
    return x / y

    # this function will divide x by y, but right before it will check if y is 0
    # in python division by zero is undefinded and so the function will return the
    # message "ERROR: CANNOT DIVIDE BY ZERO" prompting line 19 of the code to run

    
    # lines 28 - 40 (12 lines of code below this)
    # prompts the user to enter 2 different numbers 
    # along w/ what operation they would wanna choose
    # such as: addition, subtraction, multiplication, division

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # calculation function and displaying to user to choose one of options

    while True:

        # while loop that runs forever until the user decides to exit program.

        choice = input("Enter choice (1/2/3/4): ")

        # input() function asking user to choose an operation, 
        # then choice stores the users input as a variable

        # can use input and attach any name

        if choice in ('1', '2', '3', '4'):

            # checks if the user has made a valid choice

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # these lines ask the user to input 2 numbers
            # The float() function is used to make sure the user is able
            # to enter both integers and decimals
            # and then the user inputs are stored as variables num1 and num2

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

                # If the user enters 1 this line will print the result of num1 & num2
                # Then it calls upon the addition function to perform the calculation

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

            # line will print if user enters an invalid choice

        next_calculation = input("Do you want another calculation? (yes/no): ")

            # prompting the user asking if they would want to perform another function
            # then their response is stored with in the variable above.

        if next_calculation.lower() != 'yes':
            break

            # based off the input of the user that was stored in the next function above
            # if the user does not type "yes" the program will break out of the loop thus
            # ending the caluclator program
            # 
            # also, the .lower() function makes sure that the user does not get penalized for
            # making it upper and or lower case.

# Run the calculator
calculator()

# runs the calculator function, thus, starting the program

