"""class docstring """
class dog:
    """ A simple dog class to represent a dog 
    """
    def ___init__(self,name):
        self.name = name 
    def bark(self):
        return f"{self.name} sayas woof"
print(dog.__doc__)

