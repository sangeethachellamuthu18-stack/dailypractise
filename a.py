class destructor:
    def __init__(self):
        print("its a constructor method")
    
    def __del__(self):
        print("its a destructor method")

a=destructor()