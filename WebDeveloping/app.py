__author__ = "janao"

def age_program():
    user_age = input("Enter your age: ")
    age_second = int(user_age) + 365*24*60*60
    print("Your age in seconds in {}".format(age_second))

age_program()