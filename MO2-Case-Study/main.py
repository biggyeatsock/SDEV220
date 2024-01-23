############################################
#  File name: Main.py
#  
#  A simple program to determine if a student
#  has made the Dean's list of if they made honor Roll
#
#  Author: Logan Luper
#
#  Date: Jan. 23rd, 2024
#
#############################################


def get_user_input():  # obtains user input while checking for a valid response
    userinput = input("Enter a student's last name:\n > ")
    if userinput == "ZZZ":
        print("\nGoodbye!")
        exit()

    while userinput == "":
        print("Invalid input. \nPlease enter a student's last name:")
        userinput = input('> ')
    
    return userinput


def get_grade(userinput):  # obtains grade from user input
    grade = float(input(f"Enter the grade for {userinput}:\n > "))
    while grade == "":
        print("Invalid input. \nPlease enter the grade for the student:")
        grade = input('> ')
    return grade



def main():
    name = get_user_input()
    grade = get_grade(name)

    if grade >= 3.5:
        print(f"Congratulations, {name}, you have made the Dean's List")

    elif grade >= 3.25:
        print(f"Congratulations, {name}, you have made the Honor Roll")

    print(f"\nThe grade for {name} is {grade}.")

main()