# Python for Beginners: Projects & Pseudocode Guide

## Part 1: Core Concepts

### 1. Variables & Data Types

**Pseudocode:**
```
DECLARE age AS integer
DECLARE name AS string
DECLARE height AS float
DECLARE is_student AS boolean

SET age = 20
SET name = "John"
PRINT age, name
```

**Python Equivalent:**
```python
age = 20
name = "John"
height = 5.9
is_student = True

print(age, name)
```

---

### 2. Conditional Statements (if/else)

**Pseudocode:**
```
INPUT score from user
IF score >= 90 THEN
    PRINT "Grade: A"
ELSE IF score >= 80 THEN
    PRINT "Grade: B"
ELSE
    PRINT "Grade: C"
END IF
```

**Python Equivalent:**
```python
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")
```

---

### 3. Loops (for & while)

**Pseudocode:**
```
FOR i = 1 TO 5 DO
    PRINT i
END FOR

SET count = 0
WHILE count < 3 DO
    PRINT "Hello"
    count = count + 1
END WHILE
```

**Python Equivalent:**
```python
# For loop
for i in range(1, 6):
    print(i)

# While loop
count = 0
while count < 3:
    print("Hello")
    count = count + 1
```

---

### 4. Lists & Loops

**Pseudocode:**
```
CREATE list fruits = ["apple", "banana", "orange"]

FOR each fruit IN fruits DO
    PRINT fruit
END FOR
```

**Python Equivalent:**
```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

---

### 5. Functions

**Pseudocode:**
```
FUNCTION add(a, b)
    RETURN a + b
END FUNCTION

result = add(5, 3)
PRINT result
```

**Python Equivalent:**
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

---

## Part 2: Beginner Projects

### Project 1: Simple Calculator

**Pseudocode:**
```
INPUT num1 from user
INPUT operation from user (+, -, *, /)
INPUT num2 from user

IF operation == "+" THEN
    result = num1 + num2
ELSE IF operation == "-" THEN
    result = num1 - num2
ELSE IF operation == "*" THEN
    result = num1 * num2
ELSE IF operation == "/" THEN
    IF num2 != 0 THEN
        result = num1 / num2
    ELSE
        PRINT "Cannot divide by zero"
    END IF
END IF

PRINT result
```

**What you'll learn:** Input/output, conditionals, basic arithmetic

---

### Project 2: Number Guessing Game

**Pseudocode:**
```
IMPORT random

secret_number = random.integer between 1 and 100
guess = 0
attempts = 0

WHILE guess != secret_number DO
    INPUT guess from user
    attempts = attempts + 1
    
    IF guess < secret_number THEN
        PRINT "Too low, try again"
    ELSE IF guess > secret_number THEN
        PRINT "Too high, try again"
    ELSE
        PRINT "You won in " + attempts + " attempts!"
    END IF
END WHILE
```

**What you'll learn:** Loops, random numbers, conditionals, variables

---

### Project 3: To-Do List

**Pseudocode:**
```
CREATE empty list tasks

WHILE true DO
    PRINT menu
    INPUT choice from user
    
    IF choice == "1" THEN
        INPUT new_task from user
        ADD new_task TO tasks
    ELSE IF choice == "2" THEN
        PRINT all tasks with numbers
    ELSE IF choice == "3" THEN
        INPUT task_number to remove
        REMOVE task at task_number from tasks
    ELSE IF choice == "4" THEN
        BREAK (exit loop)
    END IF
END WHILE
```

**What you'll learn:** Lists, loops, user input, list manipulation

---

### Project 4: Temperature Converter

**Pseudocode:**
```
FUNCTION celsius_to_fahrenheit(celsius)
    RETURN (celsius * 9/5) + 32
END FUNCTION

FUNCTION fahrenheit_to_celsius(fahrenheit)
    RETURN (fahrenheit - 32) * 5/9
END FUNCTION

INPUT temperature from user
INPUT unit from user (C or F)

IF unit == "C" THEN
    result = celsius_to_fahrenheit(temperature)
    PRINT result + " Fahrenheit"
ELSE
    result = fahrenheit_to_celsius(temperature)
    PRINT result + " Celsius"
END IF
```

**What you'll learn:** Functions, conditionals, basic math

---

### Project 5: Word Frequency Counter

**Pseudocode:**
```
INPUT text from user
CREATE empty dictionary word_count

SPLIT text into words
FOR each word IN words DO
    CONVERT word to lowercase
    REMOVE punctuation
    
    IF word exists in word_count THEN
        word_count[word] = word_count[word] + 1
    ELSE
        word_count[word] = 1
    END IF
END FOR

FOR each word and count IN word_count DO
    PRINT word + ": " + count
END FOR
```

**What you'll learn:** Dictionaries, loops, string manipulation

---

## Part 3: Project Progression Path

1. **Start with:** Simple Calculator
2. **Then:** Number Guessing Game
3. **Progress to:** Temperature Converter
4. **Then:** To-Do List
5. **Finally:** Word Frequency Counter

---

## Tips for Success

✓ Start with pseudocode before writing Python  
✓ Test your code with different inputs  
✓ Break big problems into smaller functions  
✓ Use meaningful variable names  
✓ Add comments to explain your code  
✓ Don't skip the basics—they matter!

---

## Common Python Syntax Reminders

```python
# Comments
x = 5  # This is a comment

# Lists
my_list = [1, 2, 3]
my_list.append(4)

# Dictionaries
my_dict = {"name": "John", "age": 25}
print(my_dict["name"])

# Strings
message = "Hello " + "World"
```

Ready to start? Which project interests you most?