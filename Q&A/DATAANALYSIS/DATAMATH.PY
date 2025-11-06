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