# Python Advanced Guide: Functions, OOP, Errors, Threading, Files & Projects

---

## PART 1: FUNCTIONS IN DETAIL

### 1.1 What is a Function?
A function is a reusable block of code that performs a specific task.

**Pseudocode:**
```
FUNCTION greet(name)
    PRINT "Hello, " + name
END FUNCTION

CALL greet("Alice")
```

**Python:**
```python
def greet(name):
    print(f"Hello, {name}")

greet("Alice")  # Output: Hello, Alice
```

---

### 1.2 Function Types

#### A) Functions with No Parameters & No Return
```
FUNCTION sayHello()
    PRINT "Hello World"
END FUNCTION
```

```python
def say_hello():
    print("Hello World")

say_hello()  # Output: Hello World
```

---

#### B) Functions with Parameters (Arguments)
```
FUNCTION add(a, b)
    PRINT a + b
END FUNCTION

add(5, 3)  # Output: 8
```

```python
def add(a, b):
    print(a + b)

add(5, 3)  # Output: 8
```

---

#### C) Functions with Return Values
```
FUNCTION multiply(x, y)
    result = x * y
    RETURN result
END FUNCTION

answer = multiply(4, 5)
PRINT answer  # Output: 20
```

```python
def multiply(x, y):
    result = x * y
    return result

answer = multiply(4, 5)
print(answer)  # Output: 20
```

---

#### D) Functions with Default Parameters
```
FUNCTION introduce(name, age = 18)
    PRINT "I am " + name + " and " + age + " years old"
END FUNCTION

introduce("Bob")           # Uses default age = 18
introduce("Alice", 25)     # Uses provided age = 25
```

```python
def introduce(name, age=18):
    print(f"I am {name} and {age} years old")

introduce("Bob")        # Output: I am Bob and 18 years old
introduce("Alice", 25)  # Output: I am Alice and 25 years old
```

---

#### E) Functions with Multiple Return Values
```
FUNCTION getCoordinates()
    RETURN 10, 20
END FUNCTION

x, y = getCoordinates()
PRINT x, y  # Output: 10 20
```

```python
def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print(x, y)  # Output: 10 20
```

---

#### F) Functions with *args (Variable Arguments)
```
FUNCTION sum_all(*numbers)
    total = 0
    FOR each num IN numbers DO
        total = total + num
    END FOR
    RETURN total
END FUNCTION

result = sum_all(1, 2, 3, 4, 5)  # Output: 15
```

```python
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = sum_all(1, 2, 3, 4, 5)
print(result)  # Output: 15
```

---

#### G) Functions with **kwargs (Keyword Arguments)
```
FUNCTION print_info(**data)
    FOR each key, value IN data DO
        PRINT key + " : " + value
    END FOR
END FUNCTION

print_info(name="Alice", age=25, city="NYC")
```

```python
def print_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# Output: name: Alice, age: 25, city: NYC
```

---

### 1.3 Scope in Functions

**Local Scope** - Variables inside a function
```python
def my_function():
    x = 5  # Local variable (only exists inside function)
    print(x)

my_function()  # Output: 5
print(x)       # Error! x doesn't exist outside function
```

**Global Scope** - Variables outside a function
```python
x = 10  # Global variable

def my_function():
    print(x)  # Can access global x

my_function()  # Output: 10
print(x)       # Output: 10
```

---

### 1.4 Lambda Functions (Anonymous Functions)
```
FUNCTION square(x) = x * x  # Simple inline function

result = square(5)  # Output: 25
```

```python
# Lambda syntax: lambda parameters: expression
square = lambda x: x * x
print(square(5))  # Output: 25

# Often used with map, filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

---

### 1.5 Negative Aspects of Functions

#### A) Too Many Parameters (Hard to Use)
```python
# ❌ BAD - Too many parameters
def create_user(fname, lname, email, phone, age, city, country, zip):
    pass

# ✓ GOOD - Use a dictionary or object
def create_user(user_data):
    pass
```

#### B) No Documentation
```python
# ❌ BAD - No explanation
def calc(a, b, c):
    return a + b * c

# ✓ GOOD - Clear documentation
def calculate_total(price, tax_rate, discount):
    """
    Calculate total price with tax and discount
    Args: price, tax_rate, discount
    Returns: final price
    """
    return (price * tax_rate) - discount
```

#### C) Side Effects (Modifying Global Variables)
```python
# ❌ BAD - Modifies global variable
global_list = []

def add_item(item):
    global_list.append(item)  # Unexpected side effect

# ✓ GOOD - Return new list
def add_item(lst, item):
    return lst + [item]
```

#### D) Functions That Do Too Much
```python
# ❌ BAD - Mixing multiple tasks
def process_user():
    # Gets input
    # Validates
    # Saves to file
    # Sends email
    pass

# ✓ GOOD - Single responsibility
def get_user_input():
    pass

def validate_user(user):
    pass

def save_user(user):
    pass
```

---

## PART 2: CLASSES AND OBJECTS (OOP)

### 2.1 What are Classes and Objects?

A **class** is a blueprint for creating objects. An **object** is an instance of a class.

**Analogy:** Class = Cookie Cutter, Object = Actual Cookie

**Pseudocode:**
```
CLASS Dog
    PROPERTY name
    PROPERTY age
    
    METHOD bark()
        PRINT name + " says Woof!"
    END METHOD
END CLASS

CREATE object myDog FROM Dog
myDog.name = "Buddy"
myDog.age = 3
myDog.bark()  # Output: Buddy says Woof!
```

**Python:**
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says Woof!")

# Create object (instance)
my_dog = Dog("Buddy", 3)
my_dog.bark()  # Output: Buddy says Woof!
```

---

### 2.2 Class Components

#### A) Constructor (__init__)
Initializes an object when it's created.

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Toyota", "Blue")
print(car1.brand)  # Output: Toyota
```

#### B) Instance Variables (self.attribute)
Variables that belong to each object.

```python
class Person:
    def __init__(self, name, age):
        self.name = name    # Instance variable
        self.age = age      # Instance variable

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
print(person1.name)  # Output: Alice
print(person2.name)  # Output: Bob (different object!)
```

#### C) Methods (Functions in Classes)
```python
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

calc = Calculator()
print(calc.add(5, 3))       # Output: 8
print(calc.subtract(10, 4)) # Output: 6
```

#### D) Class Variables (Shared by All Objects)
```python
class Student:
    school = "XYZ School"  # Class variable (shared)
    
    def __init__(self, name):
        self.name = name   # Instance variable

student1 = Student("Alice")
student2 = Student("Bob")

print(student1.school)  # Output: XYZ School
print(student2.school)  # Output: XYZ School (same for all)
```

---

### 2.3 Types of Classes

#### A) Simple Class (Basic Structure)
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display(self):
        print(f"{self.title} by {self.author}")

book = Book("Python Guide", "John")
book.display()  # Output: Python Guide by John
```

#### B) Inheritance (Class inherits from another class)
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):  # Override parent method
        print(f"{self.name} barks")

dog = Dog("Max")
dog.speak()  # Output: Max barks
```

#### C) Polymorphism (Same method, different behavior)
```python
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

def animal_sound(animal):
    print(animal.speak())

cat = Cat()
dog = Dog()

animal_sound(cat)  # Output: Meow
animal_sound(dog)  # Output: Woof
```

#### D) Encapsulation (Hide internal details)
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private (__ prefix)
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)     # Error! Private variable
```

#### E) Abstract Class (Template for other classes)
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

car = Car()
car.start()  # Output: Car started
```

---

## PART 3: ERROR HANDLING

### 3.1 Types of Errors

**Pseudocode:**
```
TRY
    CODE that might cause error
CATCH ErrorType AS error
    HANDLE error
END TRY
```

**Python:**
```python
try:
    # Code that might cause error
    x = 10 / 0
except ZeroDivisionError:
    # Handle the error
    print("Cannot divide by zero!")
```

---

### 3.2 Common Error Types

#### A) Syntax Error (Code is incorrectly written)
```python
# ❌ Syntax Error - missing colon
def greet()
    print("Hello")

# ✓ Correct
def greet():
    print("Hello")
```

#### B) Name Error (Variable not defined)
```python
# ❌ Name Error
print(x)  # x not defined

# ✓ Correct
x = 5
print(x)  # Output: 5
```

#### C) Type Error (Wrong data type)
```python
# ❌ Type Error
result = "Hello" + 5

# ✓ Correct
result = "Hello" + str(5)  # Output: Hello5
```

#### D) Value Error (Wrong value)
```python
# ❌ Value Error
number = int("abc")  # Can't convert "abc" to int

# ✓ Correct
number = int("123")  # Output: 123
```

#### E) Index Error (Index out of range)
```python
# ❌ Index Error
my_list = [1, 2, 3]
print(my_list[10])  # No index 10!

# ✓ Correct
print(my_list[0])  # Output: 1
```

#### F) Key Error (Dictionary key not found)
```python
# ❌ Key Error
person = {"name": "Alice"}
print(person["age"])  # Key doesn't exist

# ✓ Correct
print(person.get("age", "Not found"))  # Output: Not found
```

---

### 3.3 Error Handling Techniques

#### A) Basic Try-Except
```python
try:
    age = int(input("Enter age: "))
except ValueError:
    print("That's not a number!")
```

#### B) Multiple Except Blocks
```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

#### C) Try-Except-Else
```python
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print(f"You entered: {x}")  # Only if no error
```

#### D) Try-Except-Finally
```python
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()  # Always executes!
```

#### E) Raising Errors
```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Age cannot be negative
```

---

## PART 4: THREADS AND PROCESSES

### 4.1 What are Threads and Processes?

**Process** - Separate program instance with own memory
**Thread** - Lightweight process, shares memory with other threads

---

### 4.2 Threading (Multiple threads in one process)

**Pseudocode:**
```
THREAD thread1 = create_thread(function1)
THREAD thread2 = create_thread(function2)

START thread1
START thread2

WAIT for both threads to complete
```

**Python:**
```python
import threading
import time

def task1():
    for i in range(3):
        print("Task 1 running")
        time.sleep(1)

def task2():
    for i in range(3):
        print("Task 2 running")
        time.sleep(1)

# Create threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Start threads
thread1.start()
thread2.start()

# Wait for completion
thread1.join()
thread2.join()

print("Both tasks completed!")
```

---

### 4.3 Processes (Separate programs)

**Pseudocode:**
```
PROCESS process1 = create_process(function1)
PROCESS process2 = create_process(function2)

START process1
START process2

WAIT for completion
```

**Python:**
```python
from multiprocessing import Process

def worker(name):
    print(f"Worker {name} started")
    print(f"Worker {name} finished")

if __name__ == "__main__":
    process1 = Process(target=worker, args=("A",))
    process2 = Process(target=worker, args=("B",))
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()
    
    print("All processes completed!")
```

---

### 4.4 Thread vs Process

| Feature | Thread | Process |
|---------|--------|---------|
| Speed | Fast | Slower |
| Memory | Shared | Separate |
| Communication | Easy | Complex |
| Scalability | Limited | Better |
| Crashes | Affects all | Independent |

---

## PART 5: WORKING WITH FILES

### 5.1 File Operations

**Pseudocode:**
```
OPEN file "data.txt" for reading
READ all content
CLOSE file

PRINT content
```

**Python:**
```python
# Reading a file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

---

### 5.2 File Modes

| Mode | Meaning |
|------|---------|
| "r" | Read (file must exist) |
| "w" | Write (creates/overwrites file) |
| "a" | Append (adds to end) |
| "x" | Create (fails if exists) |
| "rb" | Read binary |
| "wb" | Write binary |

---

### 5.3 Reading Files

#### A) Read All Content
```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

#### B) Read Line by Line
```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
```

#### C) Read All Lines into List
```python
with open("data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
```

---

### 5.4 Writing Files

#### A) Write (Overwrites)
```python
with open("data.txt", "w") as file:
    file.write("Hello World\n")
    file.write("Python is awesome")
```

#### B) Append (Adds to end)
```python
with open("data.txt", "a") as file:
    file.write("\nNew line added")
```

#### C) Write Multiple Lines
```python
lines = ["Line 1", "Line 2", "Line 3"]

with open("data.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
```

---

### 5.5 Working with Different File Types

#### A) CSV Files
```python
import csv

# Read CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Write CSV
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])
```

#### B) JSON Files
```python
import json

# Read JSON
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)

# Write JSON
data = {"name": "Alice", "age": 25}
with open("data.json", "w") as file:
    json.dump(data, file)
```

#### C) Text Files
```python
# Read
with open("text.txt", "r") as file:
    content = file.read()

# Write
with open("text.txt", "w") as file:
    file.write("Hello World")
```

---

## PART 6: PROJECTS

### PROJECT 1: Bank Account Manager (Functions + Classes)
**Concepts:** Classes, methods, error handling, files

**Pseudocode:**
```
CLASS BankAccount
    PROPERTY account_number
    PROPERTY balance
    
    METHOD deposit(amount)
        IF amount > 0 THEN
            balance = balance + amount
            RETURN "Deposit successful"
        ELSE
            RETURN "Invalid amount"
    END METHOD
    
    METHOD withdraw(amount)
        IF amount > 0 AND amount <= balance THEN
            balance = balance - amount
            RETURN "Withdrawal successful"
        ELSE
            RETURN "Invalid amount or insufficient funds"
    END METHOD
    
    METHOD get_balance()
        RETURN balance
    END METHOD
    
    METHOD save_to_file()
        WRITE account_number and balance to file
    END METHOD
END CLASS

MAIN
    CREATE account = new BankAccount()
    
    WHILE true DO
        PRINT menu
        INPUT choice
        
        IF choice == 1 THEN
            INPUT amount
            CALL account.deposit(amount)
        ELSE IF choice == 2 THEN
            INPUT amount
            CALL account.withdraw(amount)
        ELSE IF choice == 3 THEN
            PRINT account.get_balance()
        ELSE IF choice == 4 THEN
            CALL account.save_to_file()
        END IF
    END WHILE
END MAIN
```

**Topics Covered:** Classes, methods, error handling, file I/O

---

### PROJECT 2: Multi-threaded Download Manager (Threading)
**Concepts:** Threading, file I/O, functions

**Pseudocode:**
```
FUNCTION download_file(url, filename)
    PRINT "Downloading " + filename
    SLEEP 2 seconds (simulating download)
    SAVE file
    PRINT filename + " completed"
END FUNCTION

MAIN
    CREATE list of files to download
    
    FOR each file DO
        CREATE new thread for download
        START thread
    END FOR
    
    WAIT for all threads to complete
    PRINT "All downloads completed"
END MAIN
```

**Topics Covered:** Threading, functions, file operations

---

### PROJECT 3: Student Management System (OOP + Files + Error Handling)
**Concepts:** Classes, inheritance, JSON files, error handling, functions

**Pseudocode:**
```
CLASS Person
    PROPERTY name
    PROPERTY age
END CLASS

CLASS Student EXTENDS Person
    PROPERTY student_id
    PROPERTY courses
    PROPERTY grades
    
    METHOD add_course(course_name)
        ADD course to courses list
    END METHOD
    
    METHOD add_grade(course_name, grade)
        ADD grade for course
    END METHOD
    
    METHOD get_average_grade()
        CALCULATE and RETURN average
    END METHOD
END CLASS

CLASS StudentManager
    PROPERTY students_list
    
    METHOD add_student(student)
        ADD to list
        SAVE to JSON file
    END METHOD
    
    METHOD search_student(student_id)
        FIND and RETURN student
    END METHOD
    
    METHOD load_from_file()
        READ from JSON file
        CREATE student objects
    END METHOD
END CLASS
```

**Topics Covered:** Classes, inheritance, JSON files, error handling, file I/O

---

### PROJECT 4: Log File Analyzer (File I/O + Functions)
**Concepts:** File operations, string methods, error handling

**Pseudocode:**
```
FUNCTION read_log_file(filename)
    TRY
        OPEN file
        READ all lines
        RETURN lines
    CATCH error
        PRINT "Error reading file"
        RETURN empty list
    END TRY
END FUNCTION

FUNCTION count_errors(lines)
    count = 0
    FOR each line IN lines DO
        IF line CONTAINS "ERROR" THEN
            count = count + 1
        END IF
    END FOR
    RETURN count
END FUNCTION

FUNCTION generate_report(filename)
    lines = read_log_file(filename)
    error_count = count_errors(lines)
    
    WRITE report to new file:
        "Total lines: " + total
        "Error count: " + error_count
        "Error percentage: " + percentage
END FUNCTION

MAIN
    INPUT log_filename
    CALL generate_report(log_filename)
    PRINT "Report generated"
END MAIN
```

**Topics Covered:** File I/O, error handling, string manipulation, functions

---

### PROJECT 5: Task Scheduler with Threads (Threading + Classes + Files)
**Concepts:** Threading, classes, file I/O, error handling

**Pseudocode:**
```
CLASS Task
    PROPERTY task_id
    PROPERTY description
    PROPERTY scheduled_time
    
    METHOD execute()
        PRINT "Executing: " + description
    END METHOD
END CLASS

CLASS TaskScheduler
    PROPERTY tasks_list
    PROPERTY threads_list
    
    METHOD add_task(task)
        ADD task to list
        SAVE to file
    END METHOD
    
    METHOD schedule_tasks()
        FOR each task DO
            CREATE thread for task
            START thread
        END FOR
    END METHOD
    
    METHOD load_from_file()
        READ tasks from file
        CREATE task objects
    END METHOD
END CLASS

MAIN
    CREATE scheduler = new TaskScheduler()
    scheduler.load_from_file()
    
    PRINT menu
    WHILE choice != 4 DO
        IF choice == 1 THEN
            INPUT task details
            CREATE new task
            scheduler.add_task(task)
        ELSE IF choice == 2 THEN
            scheduler.schedule_tasks()
        ELSE IF choice == 3 THEN
            PRINT all tasks
        END IF
    END WHILE
END MAIN
```

**Topics Covered:** Threading, classes, file I/O, error handling, methods

---

### PROJECT 6: E-Commerce Order System (OOP + Error Handling + Files + Threads)
**Concepts:** Classes, inheritance, error handling, JSON files, threading

**Pseudocode:**
```
CLASS Product
    PROPERTY product_id
    PROPERTY name
    PROPERTY price
    PROPERTY stock
    
    METHOD check_availability(quantity)
        IF quantity <= stock THEN
            RETURN true
        ELSE
            RETURN false
    END METHOD
END CLASS

CLASS Order
    PROPERTY order_id
    PROPERTY products
    PROPERTY total_price
    
    METHOD calculate_total()
        total = 0
        FOR each product IN products DO
            total = total + product.price
        END FOR
        RETURN total
    END METHOD
END CLASS

CLASS OrderProcessor
    PROPERTY orders_list
    
    METHOD process_order(order) IN THREAD
        TRY
            VALIDATE order
            UPDATE inventory
            SAVE to JSON file
            PRINT "Order processed"
        CATCH error
            PRINT "Error processing order"
        END TRY
    END METHOD
    
    METHOD process_multiple_orders(orders_list)
        FOR each order IN orders_list DO
            CREATE thread for process_order()
            START thread
        END FOR
    END METHOD
END CLASS
```

**Topics Covered:** All concepts - Classes, inheritance, error handling, files, threading

---

## SUMMARY OF LEARNING PATH

1. **Functions** - Master function basics, parameters, returns, *args, **kwargs
2. **Classes & OOP** - Learn objects, inheritance, polymorphism, encapsulation
3. **Error Handling** - Try-except, raise, finally, custom errors
4. **Threading** - Create threads, manage concurrency, thread safety
5. **Files** - Read/write text, CSV, JSON files
6. **Projects** - Combine all concepts in real-world applications

---

## Practice Tips

✓ Start with simple functions, gradually add complexity
✓ Create classes for real-world objects (Person, Car, Book)
✓ Always handle errors - expect things to go wrong
✓ Use threading for I/O-bound tasks (file reading, network)
✓ Save/load data to files to persist information
✓ Build projects combining multiple concepts
✓ Test your code with different inputs
✓ Read error messages carefully - they help you debug!

Ready to code? Pick a project and let's build it together! 🚀