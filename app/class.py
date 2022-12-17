# class
class Person:
    #class attributes
    address = 'no info'
    #constructor
    def __init__(self, name, year):
        #object attributes
        self.name = name
        self.year = year
        
        #methods

# object (instance)
p1 = Person(name='fatih',year='1999')
p2 = Person('burak','1995')

#updating
p1.name = 'ahmet'

#accessing object attributes
print(f"p1 - name:{p1.name} year:{p1.year} address: {p1.address}")
print(f"p2 - name:{p2.name} year:{p2.year}")

