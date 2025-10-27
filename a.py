"""
class destructor:
    def __init__(self):
        print("its a constructor method")
    
    def __del__(self):
        print("its a destructor method")

a=destructor()
"""
import sys
x=12
y="This function returns the size (in bytes) of a Python object."
print("x", sys.getsizeof(x)) 
print("y",sys.getsizeof(y))