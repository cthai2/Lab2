"""
Author: Chris Thai
SDEV300-6381
August 30, 2022,
Purpose: To produce a command line menu-driven python application providing
users with the ability to perform some math and security related functions
"""

import string
import secrets
import math
import sys
from datetime import datetime, date, time
from threading import Event


def get_password(length):
    """Defining Menu selection 1"""
    alphanumeric = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    while True:
        password = ''.join(secrets.choice(alphanumeric) for i in range(20))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    return password


def get_percentage(numer, deno, dec):
    """Defining Menu selection 2"""
    percentage = (numer / deno) * 100
    return round(percentage, dec)


def days_to_2025_7_04():
    """Defining Menu selection 3"""
    today = str(date.today())
    other = '2025-7-04'
    date1 = datetime.strptime(today, "%Y-%m-%d")
    date2 = datetime.strptime(other, "%Y-%m-%d")
    return abs((date2 - date1).days)


def law_of_cosine(length_a, length_b, degree_c):
    """Defining Menu selection 4"""
    c2 = (length_a ** 2) + (length_b ** 2) - (2 * length_a * length_b * (math.cos(degree_c)))
    side_c = math.sqrt(c2)
    return round(side_c, 5)


def volume_of_cylinder(length_radius, length_height):
    """Defining Menu selection 5"""
    volume = (math.pi * (length_radius ** 2)) * length_height
    return round(volume, 5)


def start():
    try:
        print("\n==========================MAIN MENU==================================")
        print("1.\tGenerate Secure Password")
        print("2.\tCalculate and Format a Percentage")
        print("3.\tHow many days from today until July 4, 2025?")
        print("4.\tUse the Law of Cosines to calculate the leg of a triangle")
        print("5.\tCalculate the volume of a Right Circular Cylinder")
        print("6.\tExit program")
        print("=====================================================================\n")

        selection = int(input("Please select an option from the main menu:\t"))

    except ValueError:
        print("\nERROR!\nPlease enter in ONLY numbers\n")
        Event().wait(1)
        start()

    while True:
        if selection == 1:
            try:
                pwd_length = int(input("Enter in a password length: \t"))
                print("Your new password is: {}\t".format(get_password(pwd_length)))
                Event().wait(2)  # number of seconds the code will delay before next line calls the function
                start()
            except ValueError:
                print("\nERROR!\nPlease enter in ONLY numbers\nGoing back to the main menu....\n")
                Event().wait(2)
                start()

        if selection == 2:
            try:
                numerator = int(input("Enter in the numerator: \t"))
                denominator = int(input("Enter in the denominator: \t"))
                decimal = int(input("Enter in the number of decimal places: \t"))

                if denominator == 0:
                    print("\nERROR!\nCan not divide by zero\nGoing back to the main menu....\n")
                    Event().wait(2)
                    start()

                elif numerator > denominator:
                    print("\nERROR!\nnumerator must be a smaller value than the denominator\n")
                    numerator = int(input("Enter in the numerator: \t"))
                    denominator = int(input("Enter in the denominator: \t"))
                    decimal = int(input("Enter in the number of decimal places: \t"))

            except ValueError:
                print("\nERROR!\nPlease enter in ONLY numbers\nGoing back to the main menu....\n")
                Event().wait(2)
                start()

            else:
                print("The percentage is: {} %\t".format(get_percentage(numerator, denominator, decimal)))
                Event().wait(2)
                start()

        if selection == 3:
            print("There are {} days left until July 4,2025".format(days_to_2025_7_04()))
            Event().wait(2)
            start()

        if selection == 4:
            try:
                side_a = int(input("Enter in side a: \t"))
                side_b = int(input("Enter in side b: \t"))
                angle_c = float(input("Enter in angle C: \t"))
            except ValueError:
                print("\nERROR!\nPlease enter in ONLY numbers\nGoing back to the main menu....\n")
                Event().wait(2)
                start()

            print("The length of side c is: {} \t".format(law_of_cosine(side_a, side_b, angle_c)))
            Event().wait(2)
            start()

        if selection == 5:
            try:
                radius = int(input("Enter in the radius of the cylinder: \t"))
                height = int(input("Enter in the height of the cylinder: \t"))
            except ValueError:
                print("\nERROR!\nPlease enter in ONLY numbers\nGoing back to the main menu....\n")
                Event().wait(2)
                start()

            print("The volume of this cylinder is:{}\t".format(volume_of_cylinder(radius, height)))
            Event().wait(2)
            start()

        if selection == 6:
            sys.exit("\nThank you for using the program. Goodbye!")

        else:
            print("ERROR: Invalid response.\n")


""" End Of Start Function """
start()
