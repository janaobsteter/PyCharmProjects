class MyClass:
    def method(self): #this is an instance method
        return "This is a plane instance method", self #through this we can modify and read attributes on the object instance

    @classmethod
    def classmethod(cls): #it does not have the self -
        #so it can not access self attributes, only the class itself (the object representing the class)
        #the attributes that exists on the class and not on the instance
        return "This is a class method", cls

    @staticmethod
    def staticmethod(): #it does not take attribute - it does not have access to instance or class attributes
        return "This is a static method"



obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())