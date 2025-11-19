import numpy as np
zeros = np.zeros(5)
zeros2d = np.zeros((3,4))
print(f" 1d {zeros} and 2d \n{zeros2d}")

# empty  array 
empty = np.empty(5)
print(f" this is empty :{empty}")
# array with specific value
full = np.full(5,7)
full2d = np.full((5,7),10) 
print(f" this is full with same  numeber : {full} and {full2d}")

# range of values 
range_arr = np.arange(0,10)
range_step = np.arange(0,10,3)
print(f" it will find range of array {range_arr} and  if it will steps at 3 {range_step}")
# evenly spaced value 
linespace = np.linspace(0,1,5)
print(f" it eill fine linespace of float value {linespace}")