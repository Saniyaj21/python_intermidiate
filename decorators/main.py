# 1. Function decorator 
# 1. Class decorator 


# 1. Function decorator
def name_decorator(func):
    def wrapper():
        print('do something before execute')
        func()
        print('do something after execute')
    
    return wrapper

@name_decorator
def printName():
    print('Saniyaj')

printName()

# 2nd example
def sum_decorator(func):
    def wrapper(*args, **kwargs):
        print('do something before execute')
        result = func(*args, **kwargs)
        print('do something after execute')
        return result
    
    return wrapper

# decorator are the function in python
@sum_decorator
def printsum(x):
    print(x+x)

printsum(5)

















