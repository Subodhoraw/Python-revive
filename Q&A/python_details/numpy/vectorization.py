import time 
import numpy as np

# slow methode
def slow_function(n):
    result = []
    for i in range(n):
        result.append(i **2)
    return result

# fast methode 
def fast_function(n):
    arr = np.arange(n)
    return arr**2

n = 10000
start = time.time()
slow_result =  slow_function(n)
print(f" loop time:{time.time() - start: .4f}s")


start = time.time()
fast_result = fast_function(n)
print(f"NumPy time: {time.time() - start:.4f}s")