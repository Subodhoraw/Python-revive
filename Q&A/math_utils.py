def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
print("math_utils.py__name__is",__name__)

if __name__=="__main__":
    print("running math_utils directly!")
    print("5+3 =", add(5,3))
else:
    print("imported successsfully")