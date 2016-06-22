# Main Program

#Include BMI function file
from bmi import *

#Include Retirement function file
from retirement import *

#Include Distance formula file
from distanceformula import *

loop = True

def print_menu():
    print("Function Menu")
    print("-------------")
    print("1.) Body Mass Index")
    print("2.) Retirement")
    print("3.) Distance Formula")
    print("0.) Quit")
    print('')

while loop == True:
    try:
        print_menu()
        function_choice = int(input("Enter valid Function choice: "))
    except:
        print("Enter valid choice")
    else:
        if function_choice == 1:
            print("")
            print("Body Mass Index")
            print("---------------")
            feet = input("Enter height in feet (as a integer): ")
            inches = input("Enter remaining height in inches (as an integer): ")
            weight = input("Enter weight in pounds: ")
            result = BMI(feet, inches, weight)
            if result == "invalid":
                print("Invalid - Please enter valid input")
                print("")
            else:
                print("BMI Result: You are ", result)
                print("")
        
        elif function_choice == 2:
            age = input("Enter your current age: ")
            annual_sal = input("Enter your annual salary: ")
            percentage = input("Enter the percent you wish to save from your annual salary (integer only):")
            goal = input("What is your desired goal for your retirement savings?")
            result = calucate_years_to_goal (age, annual_sal, percentage, goal)
            print(result)
            
        elif function_choice == 3:
            x1 = input("Enter the x value of the first value pair: ")
            y1 = input("Enter the y value of the first value pair: ")
            x2 = input("Enter the x value of the second value pair: ")
            y2 = input("Enter the y value of the second value pair: ")
            result = DistanceFormula(x1, y1, x2, y2)
            if (result != "Invalid Input"):
                result = "{0:.2f}".format(result)
                print("The distance between the two points is ", result)

        elif function_choice == 0:
            print("Program ended.")
            break

            
            


