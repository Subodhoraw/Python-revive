# Python Methods & Functions Cheatsheet

## String Methods (`.method()`)

### `.strip()`
Removes whitespace from the beginning and end of a string.
```python
text = "  Hello World  "
print(text.strip())  # Output: "Hello World"
```

### `.replace(old, new)`
Replaces all occurrences of a substring with another substring.
```python
text = "I love Python"
print(text.replace("Python", "Java"))  # Output: "I love Java"
```

### `.split(separator)`
Splits a string into a list of words/parts based on a separator.
```python
text = "apple,banana,orange"
fruits = text.split(",")  # Output: ['apple', 'banana', 'orange']
```

### `.join(list)`
Combines a list of strings into one string with a separator.
```python
fruits = ['apple', 'banana', 'orange']
result = ", ".join(fruits)  # Output: "apple, banana, orange"
```

### `.lower()`
Converts all characters to lowercase.
```python
text = "HELLO"
print(text.lower())  # Output: "hello"
```

### `.upper()`
Converts all characters to uppercase.
```python
text = "hello"
print(text.upper())  # Output: "HELLO"
```

### `.find(substring)`
Returns the index (position) of a substring. Returns -1 if not found.
```python
text = "Hello World"
print(text.find("World"))  # Output: 6
print(text.find("xyz"))    # Output: -1
```

### `.startswith(prefix)`
Checks if a string starts with a specific prefix. Returns True or False.
```python
text = "Hello World"
print(text.startswith("Hello"))  # Output: True
print(text.startswith("World"))  # Output: False
```

### `.endswith(suffix)`
Checks if a string ends with a specific suffix. Returns True or False.
```python
text = "Hello.txt"
print(text.endswith(".txt"))  # Output: True
```

### `.count(substring)`
Counts how many times a substring appears in a string.
```python
text = "banana"
print(text.count("a"))  # Output: 3
```

---

## List Methods (`.method()`)

### `.append(item)`
Adds an item to the end of a list.
```python
fruits = ['apple', 'banana']
fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'orange']
```

### `.remove(item)`
Removes the first occurrence of an item from the list.
```python
fruits = ['apple', 'banana', 'orange']
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'orange']
```

### `.pop(index)`
Removes and returns an item at a specific index. If no index given, removes last item.
```python
fruits = ['apple', 'banana', 'orange']
removed = fruits.pop(1)  # Removes 'banana'
print(removed)  # Output: 'banana'
print(fruits)   # Output: ['apple', 'orange']
```

### `.insert(index, item)`
Inserts an item at a specific position in the list.
```python
fruits = ['apple', 'orange']
fruits.insert(1, 'banana')
print(fruits)  # Output: ['apple', 'banana', 'orange']
```

### `.sort()`
Sorts the list in ascending order (modifies the original list).
```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5]
```

### `.reverse()`
Reverses the order of items in the list.
```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]
```

### `.index(item)`
Returns the index (position) of the first occurrence of an item.
```python
fruits = ['apple', 'banana', 'orange']
print(fruits.index('banana'))  # Output: 1
```

### `.count(item)`
Counts how many times an item appears in the list.
```python
numbers = [1, 2, 2, 3, 2, 4]
print(numbers.count(2))  # Output: 3
```

### `.clear()`
Removes all items from the list.
```python
fruits = ['apple', 'banana', 'orange']
fruits.clear()
print(fruits)  # Output: []
```

### `.copy()`
Creates a copy of the list.
```python
original = [1, 2, 3]
duplicate = original.copy()
duplicate.append(4)
print(original)   # Output: [1, 2, 3]
print(duplicate)  # Output: [1, 2, 3, 4]
```

---

## Dictionary Methods (`.method()`)

### `.get(key, default)`
Gets the value of a key. Returns default if key doesn't exist.
```python
person = {"name": "John", "age": 25}
print(person.get("name"))           # Output: "John"
print(person.get("city", "Unknown")) # Output: "Unknown"
```

### `.keys()`
Returns all the keys in a dictionary.
```python
person = {"name": "John", "age": 25}
print(person.keys())  # Output: dict_keys(['name', 'age'])
```

### `.values()`
Returns all the values in a dictionary.
```python
person = {"name": "John", "age": 25}
print(person.values())  # Output: dict_values(['John', 25])
```

### `.items()`
Returns all key-value pairs as tuples.
```python
person = {"name": "John", "age": 25}
print(person.items())  # Output: dict_items([('name', 'John'), ('age', 25)])
```

### `.update(another_dict)`
Adds or updates items from another dictionary.
```python
person = {"name": "John"}
person.update({"age": 25, "city": "NYC"})
print(person)  # Output: {"name": "John", "age": 25, "city": "NYC"}
```

### `.pop(key, default)`
Removes a key and returns its value.
```python
person = {"name": "John", "age": 25}
age = person.pop("age")
print(age)     # Output: 25
print(person)  # Output: {"name": "John"}
```

### `.clear()`
Removes all items from the dictionary.
```python
person = {"name": "John", "age": 25}
person.clear()
print(person)  # Output: {}
```

---

## Built-in Functions

### `len()`
Returns the length (number of items) of a string, list, or dictionary.
```python
print(len("Hello"))         # Output: 5
print(len([1, 2, 3]))       # Output: 3
print(len({"a": 1, "b": 2}))  # Output: 2
```

### `range(start, stop, step)`
Creates a sequence of numbers.
```python
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):   # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

### `int()`, `str()`, `float()`
Converts between data types.
```python
print(int("25"))        # Output: 25
print(str(25))          # Output: "25"
print(float("3.14"))    # Output: 3.14
```

### `type()`
Returns the data type of a value.
```python
print(type(25))         # Output: <class 'int'>
print(type("Hello"))    # Output: <class 'str'>
print(type([1, 2, 3]))  # Output: <class 'list'>
```

### `max()`, `min()`
Returns the maximum and minimum values.
```python
print(max([1, 5, 3, 9, 2]))  # Output: 9
print(min([1, 5, 3, 9, 2]))  # Output: 1
```

### `sum()`
Returns the sum of all numbers in a list.
```python
print(sum([1, 2, 3, 4, 5]))  # Output: 15
```

### `sorted()`
Returns a new sorted list without modifying the original.
```python
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 1, 3, 4, 5]
print(numbers)         # Output: [3, 1, 4, 1, 5] (unchanged)
```

### `reversed()`
Returns a reversed version of a list.
```python
numbers = [1, 2, 3, 4, 5]
print(list(reversed(numbers)))  # Output: [5, 4, 3, 2, 1]
```

### `print()`
Outputs text or values to the screen.
```python
print("Hello World")
print(25, "apples")  # Output: 25 apples
```

### `input()`
Gets user input from the keyboard as a string.
```python
name = input("What's your name? ")
print("Hello " + name)
```

### `abs()`
Returns the absolute value (removes negative sign).
```python
print(abs(-5))   # Output: 5
print(abs(3.14)) # Output: 3.14
```

### `round()`
Rounds a number to the nearest integer or decimal place.
```python
print(round(3.7))      # Output: 4
print(round(3.14159, 2))  # Output: 3.14
```

---

## Summary Table

| Type | Method | What It Does |
|------|--------|--------------|
| String | `.strip()` | Remove spaces from ends |
| String | `.replace()` | Replace text |
| String | `.split()` | Break into parts |
| String | `.join()` | Combine into one string |
| String | `.upper()` / `.lower()` | Change case |
| List | `.append()` | Add item to end |
| List | `.remove()` | Delete an item |
| List | `.pop()` | Remove and return item |
| List | `.sort()` | Sort items |
| Dict | `.get()` | Get value safely |
| Dict | `.keys()` | Get all keys |
| Dict | `.values()` | Get all values |
| Built-in | `len()` | Count items |
| Built-in | `range()` | Create sequence |
| Built-in | `type()` | Check data type |

---

## Quick Examples to Practice

```python
# String example
sentence = "  Python is awesome  "
clean = sentence.strip().lower()
print(clean)  # Output: "python is awesome"

# List example
tasks = []
tasks.append("Study")
tasks.append("Code")
tasks.extend(["Rest", "Exercise"])
print(len(tasks))  # Output: 4

# Dictionary example
student = {"name": "Alice", "grade": "A"}
print(student.get("name"))
student.update({"age": 16})
```