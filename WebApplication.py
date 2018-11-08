#strings
print("Hello")
"Hello" #if you type it in, it gives you the values of the string - what the string is witht he quotation marks
#if you use print, it prints out the string

#format
age = 5
months = 11
print ( "I am " + str(5) + " years old.")
print("I am {} years old".format(age))
print("I am {} years and {} month old".format(age, months))

print("I am {age} years old, are you {age} years old as well?".format(age=age))

#input
age = int(input("Enter you age [years]: "))
seconds = age * 365 * 24 *60 *60
print("You are {} seconds old.".format(seconds))

#method
def age_in_seconds():
    age = int(input("Enter you age [years]: "))
    seconds = age * 365 * 24 * 60 * 60
    print("You are {} seconds old.".format(seconds))

def age_in_years():
    age = int(input("Enter you age [seconds]: "))
    years = age / 365 / 24 / 60 / 60
    print("You are {} years old.".format(years))


age_in_seconds()

#'if' tests all the conditions, whereas elif (else) tests only as many as needed- until the first positive

def age_program():
    pref = input("Input in seconds [s] or years [y]? ")
    if pref == "y":
        #convert years to second
        age_in_seconds()
    elif pref == "s":
        #convert seconds to years
        age_in_years()

age_program()


#lottery
from random import randint

def user_guess():
    return int(input("Choose a number between 0 and 10: "))

number = randint(0, 10)
def check_guess(number, guess):
    if number == guess:
        return "You won!"
    else:
        choice = input("Wrong number. Try again [y/n]? ")
        if choice == "y":
            check_guess(number, user_guess())
        else:
            exit

check_guess(number, user_guess())