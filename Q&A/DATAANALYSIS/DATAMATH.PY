numbers = [70,30,50,80,90]
mean = sum(numbers)/ len(numbers)
print(mean) # it print the mean oh numbers 
#methode 2 with statics library 
import statistics
mean = statistics.mean(numbers)
print(mean)
# method using numpy
import numpy as np 
mean = np.mean(numbers)
print(mean)
#using pandas 
import pandas as pd
df = pd.DataFrame({'scores':[70,30,50,80,90]}) 
mean= df['scores'].mean()

"""MEDIANS """
Number = [5,6,7,8,9]
median = statistics.median(Number)
print(f"Median:{median}")

#even numbers of value
num1 = [10,30,40,50]
median = statistics.median(num1)
print(f"Median of even:{median}")

median = np.median(num1) # uing numpy
print(f" median using numpy : {median}")
median = pd.Series(num1).median()
print(f" median using pandas: {median}")

"""Mode """
num2 = [2,3,4,5,6,4,5,6,2,4,56,7]
mode = statistics.mode(num2)
print(mode)

#pandas
mode = pd.Series(num2)
print(mode)
#from scipy 
from scipy import stats
mode = stats.mode(num2 , keepdims = True) ### important to learn 
print(f"Mode: {mode.mode[0]}")

""" real life example """
scores = [75, 78, 78, 39,56, 59, 56, 89]
print("===Test Scores analysis===")
print(f"Data:{scores}\n")
print(max(scores))
print(statistics.median(scores))
print(np.mean(scores))
print(pd.Series(scores))
"""range"""
sales = [ 100, 200,500,600,1200]
maximum = max(sales)
minimum = min(sales)
range_value = maximum - minimum
print(minimum)
print(maximum)
print(range_value)
# Numpy has a builtup ptp(peak to peak) function 
range_value = np.ptp(sales)
range_value = np.max(sales) - np.min(sales)
print(range_value)
### pandas
df = pd.Series(sales)
print(df.max)

""" complete analysis fiction """
def analyze_range(data):
    """ comprehensive range analysis"""
    maximum = np.max(data)
    minimum = np.min(data)
    range_value = np.ptp(data)

    print("="* 40)
    print(F"{'Range Analysis':^40}")
    print("="*40)
    print(f"Data:  {data}")
    print(f"Maximum valu: {maximum}")
    print(f"Minimum value: {minimum}")
    print(f"Range VAlue: {range_value} ")
    print(f"Interpretation : Data spans {range_value} units")
    print("="* 40)
    return range_value 

data = [ 100, 200,500,600,1200]
range_value = analyze_range(data)







