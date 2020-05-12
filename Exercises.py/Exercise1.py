from __future__ import division
from collections import defaultdict
import math
import numpy as np
import re
from operator import itemgetter, attrgetter
import random

#Question 1
print([x for x in range(2000, 3201) if x % 7 == 0 and x % 5 != 0])

#Question 2
#factorial
def factorial (x):
    if x == 1:
        return 1
    return (x * factorial (x - 1))

print(factorial(8))

#Question 3
# With a given integral number n, write a program to generate a dictionary that contains
# (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:


def quadr (number):
    q = dict()
    for n in range(1, number +1):
        q[n] = n**2
    return q

print(quadr(8))

#Question 4
# Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# values = input("Insert values: ")
# print(values.split(","))
# print(tuple(values.split(",")))

class strings(object):
    def __init__(self):
        self.input = input("Inser input: ")

    def getString(self):
        return str(self.input)

    def printStrinG(self):
        return self.getString().upper()

# a = strings()
# print(a.getString())
# print(a.printStrinG())

#question 6
def formula():
     values = input("Insert values: ")
     output = []
     C = 50
     H = 30
     for d in [float(x) for x in values.split(",")]:
         output.append(str(int(math.sqrt((2 * C * d) / H))))
     return ",".join(output)

#print(formula())


# Question 7
# Level 2
#
# Question:
# Write a program which takes 2 digits, X,Y as input and generates a
# 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

i=3
j=5
a = np.empty((i, j))


for ix in range(i):
    for ij in range(j):
        a[ix, ij] = int(ix * ij)

print(a)
print([list(x) for x in list(a)])


# Question 8:
# Write a program that accepts a comma separated sequence
# of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def orderString():
    return ",".join(sorted([x for x in input("Enter strings: ").split(",")]))

#print(orderString())

# Question 9
# Write a program that accepts sequence of lines as input
# and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

def upperRows():
    rows1 = input("Enter rows: ")
    rows2 = input("Enter rows: ")
    return  rows1.upper() + "\n" + rows2.upper()

#print(upperRows())

# Question 10:
# Write a program that accepts a sequence of whitespace separated
# words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

def removeDupl():
    return " ".join(sorted(list(set([x for x in input("Enter strings: ").split(" ")]))))

#print(removeDupl())


# Question 18:
# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

def checkPasswords():
    passwords = input("Enter passwords: ").split(",")
    return [password for password in passwords if all([bool(re.search("[a-z]", password)), bool(re.search("[0-9]", password)),
               bool(re.search("[A-Z]", password)), bool(re.search("[$#@]", password)), bool(len(password) >= 6),
                                                       bool(len(password) <= 12)])]

#print(checkPasswords())
#




# Question 19:
# You are required to write a program to sort the (name, age, height)
# tuples by ascending order where name is string, age and height are numbers.
# The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

l = []

# while True:
#     s = input("Enter tuple: ")
#     if not s:
#         break
#     l.append(tuple(s.split(",")))

#print(sorted(l, key=itemgetter(0,1,2)))


# Question 20:
# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

def generateNumbers(n):
    yield [x for x in range(n) if x % 7 == 0]

#print([x for x in generateNumbers(100)])


# Question 21
# A robot moves in a plane starting from the original point (0,0).
    # The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
    # The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance
    # from current position after a sequence of movement and original point.
    # If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5

# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

def getDistance():
    x, y = (0,0)
    while True:
        p = input("Enter direction: ")
        if not p:
            break
        way, number = tuple(p.split(" "))
        if way == "UP":
            x += float(number)
        if way == "DOWN":
            x -= float(number)
        if way == "RIGHT":
            y += float(number)
        if way == "LEFT":
            y -= float(number)
    return int(round(math.sqrt(x**2 + y**2), 0))

#print(getDistance())

# Question 22:
# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
#
# def countWords():
#     sentence = input("Enter sentence: ")
#     a = sentence.split(" ")
#     return dict([(x, a.count(x)) for x in a])
#
# z = countWords()
# for a in sorted(z):
#     print("%s:%d" % (a, z[a]))


# Question:
#
# Please write a program to output a
# random even number between 0 and 10 inclusive using random module and list comprehension.

#print(random.choice([x for x in range(11) if x % 2 == 0]))

#Minion game
import re

def minion_game(string):
    string = string.upper()
    if len(string) > 0 and len(string) < 10**6:
        vowels = list('AEIOU')
        stuart = 0
        kevin = 0
        #substrings = []
        for start in range(len(string)):
            for stop in range(start+1, len(string)+1):
                substring = string[start:stop]
                # if substring in substrings:
                #     continue
                # substrings.append(substring)
                if substring[0] in vowels:
                    kevin += 1
                if substring[0] not in vowels:
                    stuart += 1
        if kevin > stuart:
            print ("Kevin " + str(kevin))
        if kevin < stuart:
            print ("Stuart " + str(stuart))
        if kevin == stuart:
            print ("Draw")


#minion_game("BAANANAS")

# vowels = ['A', 'E', 'I', 'O', 'U']
# s = input()
# a = 0
# b = 0
# for i, c in enumerate(s):
#     if c in vowels:
#         b += len(s) - i
#     else:
#         a += len(s) - i
#
# print(a)
# print(b)
# if a == b:
#     print("Draw")
# elif a > b:
#     print('Stuart {}'.format(a))
# else:
#     print('Kevin {}'.format(b))


# def merge_the_tools(string, k):
#     t = [string[i -k: i] for i in [x for x in range(1, len(string)+1) if x % k == 0]]
#     print("substrings: " + t)
#     for tsub in t:
#         print(tsub)
#         print("".join(sorted(set(tsub), key=tsub.index)))
#
# merge_the_tools("AABCAAADA", 3)


#Squaring numbers
def square(match):
    number = int(match.group(0))
    print(number)
    return str(number**2)

#print(re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9"))

numberOfLines = input()
lines = []
while True:
    line = raw_input(9)
    if not line:
        break
    lines.append(raw_input())


# [re.sub("||", "and", line) for line in lines]
# print("\n".join(lines))

def product(fracs):
    number = int(input())
    Ts =  [tuple(map(int, input().split(" "))) for x in range(number) ]
    numerator = [c for (c,a) in Ts]
    denominator = [a for (c,a) in Ts]
    t.numetator = reduce(lambda x, y: x*y, numerator)
    t.denominator = reduce(lambda x, y: x*y, denominator)
    return t.numerator, t.denominator