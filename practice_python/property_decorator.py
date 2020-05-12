

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


tem = Celsius()
print(tem.temperature)
tem.temperature = 10
print(tem.temperature)
print(tem.to_fahrenheit())


#if you want to limit the temperature - it can not go below absolute 0

class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 not possible")
        else:
            self._temperature = value

    def get_temperature(self):
        return self._temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

tem = Celsius()
print(tem.__dict__)
print(tem._temperature)
tem.set_temperature(-30)
print(tem._temperature)
print(tem.get_temperature())
print(tem.to_fahrenheit())

#BUT if we update the class, we also have to change the code
#so we use property
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 not possible")
        print("Setting value")
        self._temperature = value

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32


    temperature = property(get_temperature, set_temperature)
    #property(fget=None, fset=None, fdel=None, doc=None)
    #this is equivalent
    temperature = property()
    temperature = temperature.getter(get_temperature)
    temperature = temperature.setter(set_temperature)


c = Celsius()
c.temperature
c.temperature = 40


#use temperature for all insted of set / get temperature
class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperatue * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return (self._temperature)

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            print("Temperature below -273 notvpossible")
            return
        print("Setting value")
        self._temperature = value

C = Celsius()
C.temperature = 30
C.temperature

#another example
class Person(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        try:
            return "Person with name {} and last name {}".format(self.name, self.surname)
        except:
            return "Person has no name and / or surname"

    @property
    def full_name(self):
        print("Getting names")
        return self.name + ' ' + self.surname

    @full_name.setter
    def full_name(self, value):
        print("Setting names")
        first_name, last_name = value.split(" ")
        self.name = first_name
        self.surname = last_name

    @full_name.deleter
    def full_name(self):
        print("Deleting names")
        del self.name
        del self.surname


me = Person("Jana", "Ob")
me
me.full_name
me.full_name = "Aleš podobnik"
me
del me.full_name
me
