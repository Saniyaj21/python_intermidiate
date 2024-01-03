# raise error
x = 0 
# if x == 0:
#     raise Exception("X is 0")

# assert (x > 0)
# assert (x > 0) , "This is a assert error, x should be gratter than 0"

# exception handling

# try:
#     a = 5 / 0
# except:
#     print("Can't devide by 0")

# try:
#     a = 5 / 0
# except Exception as e:
#     print(e)

try:
    # a = 5 / 0
    b = 5 + '10'
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print("2nd -> ", e)
else:
    print("No error")
finally:
    print("Runs every time at the end")

# creating custom error type
class SaniError (Exception):
    pass

try:
    n = 0
    if n == 0:
        raise SaniError('Custom sani error')
except SaniError as e:
    print(e)



