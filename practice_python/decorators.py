#first simply decorators
#python function can call another function
def first(msg):
    print(msg)

def second(func, value):
    return func(value)

second(first, "Hello")

#A function can return a function
def create_func():
    def is_func(value):
        print(value)
    return is_func

newF = create_func()
newF("Wow")

#decorator takes an inner function, adds some functionality and returns it!
def make_pretty(func): #make pretty is a decorator
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

ordinary()
pretty = make_pretty(ordinary) #the ordinary() function for decorator and got the name pretty
#decorator acts as a wrapper, the nature of the object (the gift) does not change, but now it looks pretty
pretty()

ordinary = make_pretty(ordinary) #this is common --> Python has a syntax for it (@)
ordinary()

#so we can use decorator instead
@make_pretty
def ordinary():
    print("I am ordinary")

#this is equivalent to
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary) #the decorator is function = decorator(function)

#function with parameters
def divide(a, b):
    return a/b
divide (2,5)
divide (2,0)


def smart_divide(func):
    def inner(a,b):
        print("I am going to divide {} and {}".format(a, b))
        if b == 0:
            print("Whoops, cannot divide with 0!")
            return
        return func(a, b)
    return inner

@smart_divide
def divide(a,b):
    return a/b

divide(5,0)

#works with any number of parameters
def works_with_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner

@works_with_all
def multiply(a,b,c,d):
    return a*b*c*d

multiply(2,3,6,7)

#chaining decorators
#a function can be decorated with multiple decorators
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

printer("Print")