#inheritance (Kalıtım)

# Person => name, lastname, age, run()
# Student(Person), Teacher(Person) 

#Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created")
    
    def who_am_i(self):
        print('i am person')

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("student created")

    #override
    def who_am_i(self):
        print("i am student")

    def sayHello(self):
        print("hi, i am student")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname,lname)
        self.branch = branch
    def who_am_i(self):
        print(f"i am a {self.branch} teacher")



p1 = Person('f','t')
s1 = Student('b','t', 2112)
t1 = Teacher('Fatih','Tarim','Math')

t1.who_am_i()
p1.who_am_i()
s1.who_am_i()
s1.sayHello()