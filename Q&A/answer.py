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

