## for loop itreate over a sequence 
## while loop

i = 0 
while i < 5:
    print(i)
    i += 1
count = 0
while count < 5:
    print(count)
    count += 1
for count in range(5):
    print(count)

""" python code for detais how does it work """
print(dir(__builtins__)) ##see all builtins names 
#inspect any object
import inspect
print(inspect.getmembers(list))

#view sourcs code 
print(inspect.getsource(sum))
