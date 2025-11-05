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