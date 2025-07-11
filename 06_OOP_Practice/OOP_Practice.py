# 01. Using self

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s = Student("M Farhan Ahmed", 95)
s.display() # Output: Name: M Farhan Ahmed, Marks: 95

# 02. Using cls

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total object created: {cls.count}")

c1 = Counter()
c2 = Counter()
c3 = Counter()
Counter.show_count() # Output: Total object created: 3

# 3. Public Variables and Methods

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car is starting...")

car1 = Car("Audi")
print(car1.brand)
car1.start()

car2 = Car("Toyota")
print(car2.brand)
car2.start()

# 4. Class Variables and Class Methods

class Bank:
    def __init__(self):
        bank_name = "Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b = Bank()
Bank.change_bank_name("NewBank")
print(b.bank_name) # Output: NewBank

# 5. Static Variables and Static Methods

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
print(MathUtils.add(6, 9)) # Output: 15

# 6. Constructors and Destructors

class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

log = Logger()
del log

# 7. Access Modifiers: Public, Private, and Protected

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # public
        self._salary = salary   # protected
        self.__ssn = ssn        # private

e = Employee("Shehroz", 50000, "123-45-6789")
print(e.name)           # ✅ Accessible
print(e._salary)        # ⚠️ Accessible but discouraged
# print(e.__ssn)        # ❌ Will raise an AttributeError
print(e._Employee__ssn)

# 8. The super() Function

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Calls Person.__init__(self, name)
        self.subject = subject

t = Teacher("Shakeel", "Math")
print(t.name, t.subject) # Output: Shakeel Math

# 9. Abstract Classes and Methods

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
r = Rectangle(10, 20)
print(r.area()) # Output: 200

# 10. Instance Methods

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

d = Dog("Buddy", "Golden Retriever")
d.bark()  # Output: Buddy says Woof!

# 11. Class Methods

class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

Book.increment_book_count()
Book.increment_book_count()
print(Book.total_books)

# 12. Static Methods

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
print(TemperatureConverter.celsius_to_fahrenheit(32))

# 13. Composition

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()

e = Engine()
c = Car(e)
c.start_car()  # Output: Engine started

# 14. Aggregation

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

emp = Employee("Ahmed")
dept = Department(emp)
print(dept.employee.name)  # Output: Ahmed

# 15. Method Resolution Order (MRO) and Diamond Inheritance

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()

# 16. Function Decorators

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def sey_hello():
    print("Hello, world!")

sey_hello()

# 16. Function Decorators

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Hamza")
print(p.greet())

# 18. Property Decorators: @property, @setter, and @deleter

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self.value = value

    @price.deleter
    def price(self):
        del self._price

p = Product(100)
print(p.price)  # prints 100
p.price = 150
print(p.price)
del p.price

# 19. callable() and __call__()

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

m = Multiplier(3)
print(callable(m))  # prints True
print(m(5))         # prints 15

# 20. Creating a Custom Exception

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age is not valid")
    print("Access granted.")

try:
    check_age(15)
except InvalidAgeError as e:
    print(f"Error: {e}")  # prints "Age is not valid"

# 21. Make a Custom Class Iterable

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

for num in Countdown(10):
    print(num)  # prints 10, 9, 8, 7,..., 1