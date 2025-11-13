## what are list comprehensions? convert a for loop that squares number into alist comprehensions. implemeent squares(n) returning [0...n-1]
list_squares = []
list = [1,2,3,4,5]
for  n in list:
    list_squares.append(n**2)
print(list_squares)
#using list comprehension
list_squares_comp = [n**2 for n in list] #list comprehension
print(list_squares_comp)
def squares(n):
    return [ i **2 for i in range(n)]
print(squares(5)) #output [0,1,4,9,16]

"""QQ how insert and append, extend work for with example """

list = [1,2,3,4,5]
list2=[1,3,5]
list.insert(1,list2)
print(list)
#append
list.append(5)
print(list)
#extend
list.extend(list2)
print(list)

""" how do you add 2 dictionaries using merge_dicts(a,b) """
dict1 ={'a':1,'b':2,'c':3,'d':5}
dict2 = {'b':4,'c':5,'d':7}
merged = dict1 | dict2
print(merged)
merge_dict = {**dict1, **dict2} #** unpack the dict
print(merge_dict) 

"""explain exception handling try/except/finally/else. Provide an example that reads and input with with exception handling """
def zero_division():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter demoniator: "))
        result = a/b
    except ZeroDivisionError:
        print("You cannot divide by zero")
        return None
    except ValueError:
        print("Please enter number only")
        return None
    else:
        print("Division Successfull")
        return result
    finally:
        print("operation completed")

print("Result:", zero_division())
"""## explain default parameter values and the mutable_default gotcha(show exaple bug) 
## what are default paramemters?
it define a fallback value for function arguement so yoou dont have to pass it everytime
Imagine a shared shopping cart 🛒 used by everyone —
if you don’t start with your own empty cart,
your items get mixed up with everyone else’s!

That’s exactly what happens when you use a mutable default in Python.
"""
def greet(name ="guest"):
    print(f"hello,{name}!")
greet("subodh")
# here is a bug 
def add_item(item, items =[]):
    items.append(item)
    return items 

#now see what happens 
print(add_item("apple"))
print(add_item("banana"))
print(add_item("cherry"))
#its wrong its gonna mess up all

## correct way
def add_item(item, items= None):
    if items is None:
        items=[] # create new list each time 
    items.append(item)
    return items
#now 
print(add_item("apple"))
print (add_item("honey"))
      
###### how dyou check the the type of an objects? compare isinstance() vs types
x = 5
print(type(x))
print(type(x)== int)
print(type(x) is int)
print(isinstance(x, int))
print(isinstance(x,(int,float)))

##in details 
class Animal:
    pass
class Dog(Animal):
    pass
my_dog = Dog()
print(type(my_dog)==Dog)
print(type(my_dog)==Animal)

print(isinstance(my_dog, Dog))
print(isinstance(my_dog, Animal))
### what are the python boolean values (True/False) How are other type thrutsy and falsey
# booleans are used for truthsy and false here is an example 
is_raining = True 
if is_raining:
    print("take an umbrella")
else:
    print("enjoy the sun")
## Example demo code 
Values = [0,1,"","hi",[],[10],None,{},{"a":1}]  
for v in Values:
    if v: 
        print(f"{repr(v):<10}  Truthy")
    else:
        print(f"{repr(v):>10}  Truthy")

#what are dict comprehension?
# convert a list to dict
# Just like list comprehensions,
"""but instead of creating a list ([]),
you create a dictionary ({}) — with key–value pairs. """
squares = {x: x**2 for x in range(5)}
print(squares)
squares = {x:x**2 for x in range(5)}
print(squares)
even_squares = { x: x**2 for x in range(5) if x%2==0}
print(even_squares)

#x = 10
y = 5
print(f" the sum od{x} and {y} is {x+y}")

name = "alice"
print(f"Uppercase:{name.upper()}") 
text = "  helo "
print(f"trimmed:{text.strip()}'")


# numnber foprmatiing 
pi = 3.14159265359
print(f"pi to 2 decimals : {pi:.2f}")
## apdding with zeros
number = 5
print(f"padded: {number:05}")
#thousand separetor 
large_number = 100000
print(f'formatted:{large_number: ,}')
# E-commerce Order Summary
def generate_order_summary():
    customer_name = "John Doe"
    order_id = 12345
    items = [
        {"name": "Laptop", "price": 999.99, "qty": 1},
        {"name": "Mouse", "price": 25.50, "qty": 2},
        {"name": "Keyboard", "price": 75.00, "qty": 1}
    ]
    
    # Calculate totals
    subtotal = sum(item["price"] * item["qty"] for item in items)
    tax_rate = 0.08
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    # Generate receipt
    print(f"{'='*50}")
    print(f"{'ORDER SUMMARY':^50}")
    print(f"{'='*50}")
    print(f"\nCustomer: {customer_name}")
    print(f"Order ID: #{order_id:06d}")
    print(f"\n{'Item':<20} {'Qty':>5} {'Price':>10} {'Total':>10}")
    print(f"{'-'*50}")
    
    for item in items:
        name = item["name"]
        qty = item["qty"]
        price = item["price"]
        line_total = price * qty
        print(f"{name:<20} {qty:>5} ${price:>9.2f} ${line_total:>9.2f}")
    
    print(f"{'-'*50}")
    print(f"{'Subtotal:':<37} ${subtotal:>9.2f}")
    print(f"{'Tax (8%):':<37} ${tax:>9.2f}")
    print(f"{'='*50}")
    print(f"{'TOTAL:':<37} ${total:>9.2f}")
    print(f"{'='*50}")
    
    # Status message with emoji and formatting
    discount_eligible = total > 1000
    print(f"\n{'🎉' if discount_eligible else '📦'} Order Status: "
          f"{'ELIGIBLE FOR DISCOUNT!' if discount_eligible else 'Processing'}")
    
    # Dynamic formatting based on total
    if total > 1000:
        savings = total * 0.10
        final_price = total - savings
        print(f"💰 You save: ${savings:.2f}")
        print(f"✨ Final price: ${final_price:.2f}")

# Run the example
generate_order_summary()
class Bankaccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount 
        return f"DEposited ${amount}. New balance: ${self.balance}"
my_account = Bankaccount(100) 
print(my_account.balance) 
print(my_account.deposit(50))
print(my_account.balance) 
class Car:
    # CLASS VARIABLE - same for all cars
    wheels = 4
    
    def __init__(self, brand, color):
        # INSTANCE VARIABLES - different for each car
        self.brand = brand
        self.color = color

# Create two cars
car1 = Car("Toyota", "red")
car2 = Car("Honda", "blue")

# Instance variables are different
print(car1.brand)  # Toyota
print(car2.brand)  # Honda
print(car1.color)  # red
print(car2.color)  # blue

# Class variable is the same for both
print(car1.wheels)  # 4
print(car2.wheels)  # 4
print(Car.wheels)   # 4 (can access via class name)