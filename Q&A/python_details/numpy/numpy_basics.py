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
arr = np.array([1,2,3,4,5,6,7])
print(arr[0])
print(arr[-1])
print(arr[1:4]) # it will slice from  1 index to 4 index before 
print(arr[:4]) # it will return till index 2 
print(arr[2:]) # it will rturn from index 2 to end 
print(arr[::2])


## basics operations 
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr + 10)
print(arr * 2)
print(arr**2)
print(arr /2)

#operation between arrays
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6]) 
print(arr1 + arr2)
print(arr1 *arr2)

# comparison operations
arr = np.array ([1,2,3,4,5])
print(arr > 3)
arr = np.array([10,202,30,40,50])

# boolean  indexing 
mask = arr > 25 
print(mask)
print(arr[mask])
#indexing directly 
print(arr[arr>10])
print(arr[(arr > 15) &(arr < 100)])

#fancy indexing 
indices = np.array([0,2,4])
arr2d = np.array([[1,3,4],
                  [9,7,9],
                  [3,5,7]])
print(arr2d[arr2d > 2])

##  array reshaping 

"""array manipulation"""

arr = np.array([[1,3,5],
                [4,5,6],
                [8,9,10]])
#reshaped = arr.reshape(5,2) ## make sure when youre reshaping matrix should match with total number ar asset
flat = arr.flatten() # flatten the array provided
print(flat)
flat = arr.ravel()# need to check 
print(flat)

#transpose

transposed = arr.T #it will transpose into t shape  means rows reshaped to column 
print(transposed)

## add dimensions
expanded = np.expand_dims(arr, axis = 0) #it willl reshape from transposed expanded  
print(expanded)

#remove dimension
squeezed = np.squeeze(expanded)
print(squeezed) #it can reshaped or squezzed to remove one dimension
arr1 = np.array([[1,3],[3,4]])
arr2 = np.array([[4,5],[2,4]])

#concatanet vertically
verticle = np.vstack([arr1,arr2])
print(verticle)
horizontal = np.concatenate([arr1,arr2])
print(horizontal)

## split
arr = np.arange(12).reshape(3,4)
split =np.split(arr,3,axis = 0)
print(split)


## stastical operations 
arr = np.array([2,3,5,6,7,8,9,10,20,40])
print(np.median(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))
print(np.sum(arr))
print(np.prod(arr))

# 2d arra 
arr = np.array([[1,3,4],
                [4,5,6]])
print(np.median(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))
print(np.sum(arr))
print(np.prod(arr))

## to learn trignometry  import numpy as np
arr = np.array([0,30,45,50,60,90])
print(np.sin(np.radians(arr)))
print(np.cos(np.radians(arr)))
print(np.tan(np.radians(arr)))

## exponentials we learnt 
arr = np.array([1,2,3,4,5,6,10])
print(np.exp(arr)) ## e = 2.71828 it will provide outcome of e to the power x = 1, 2. 3,4,5
print(np.log(arr)) # Natural log
print(np.log10(arr))
print(np.sqrt(arr))




