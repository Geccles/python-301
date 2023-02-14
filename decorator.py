def my_decorator(func):
    def wrapper():
        print("Making a taco")
        func()
        print("Finished making taco")
    return wrapper

@my_decorator
def orderTaco():
    print("Order a taco")

orderTaco()
