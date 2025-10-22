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
