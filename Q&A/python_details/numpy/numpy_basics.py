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
# specify data typee
arr_int = np.array([1,2,3],dtype = np.int32)
print(arr_int)
arr_float = np.array([1,2,3],dtype = np.float64)
print(arr_float)
arr_bool= np.array([1,2,3],dtype = bool)
print(arr_bool)
## lets go for 2d 
arr =np.array([[1,2,3,4,5],
               [1,2,3,4,5]])

print(arr[0,0])
print(arr[1,2])
print(arr[0])
print(arr[:,0])
print(arr[0:2,1:3])