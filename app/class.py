# class
class Person:
    #class attributes
    address = 'no info'
    #constructor
    def __init__(self, name, year):
        #object attributes
        self.name = name
        self.year = year
        
    # instance methods
    def intro(self):
        print("Hi there. I'm " +self.name)

    # instance methods
    def calculateAge(self):
        return 2022 - self.year

# object (instance)
p1 = Person(name='fatih',year=1999)
p2 = Person('burak',1995)

#updating
p1.name = 'ahmet'

p1.intro()

print(f'age: {p1.calculateAge()}')


class Circle:
    #Class object attribute
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap
    
    #Methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)
c1 = Circle()
c2 = Circle(5)
print(f'c1: alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}')
print(f'c2: alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}')
