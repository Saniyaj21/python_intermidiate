# tuple initializing

myTuple = ("sani", 9, False)
myTuple2 = "sani", 9, False

print(myTuple)
print(myTuple2)

# for single item in tuple
# it may be a single str a bool or int data element

t1 = ("Sani") # this is not a tuple it is a string
t2 = ("sani" ,) # this is a tuple it has a , (coma) at end

print(type(t1))

t3 = tuple(["max", 56, False, 56])
print(t2[0])
print(t3[0])


# we can run loops and check membership function

# length of tuple
print(len(t3))

# presence of element in a tuple
print(t3.count(56))
print(t3.index(56))


# conversion of list to tuple and voice versa
myList = [8]*5
myTuple = 1,2,34,5,6,7,7,8

# list to tuple
tup1 = tuple(myList)
print(tup1)

# list to tuple
lis1 = list(myTuple)
print(lis1)

# we can perform all type of slicing

# unpacking
tup2 = "sani", 19
name, age = tup2
print(name, age)
# if we take more or less value by unpacking it will give error
# n, p, o = tup2 this will give error

# using * unpacking
# * will take rest of the elements
tup3 = (91,2,3,4,5,6,6,7)
*n , m, p = tup3
print(n, m, p)




# list vs tuple

# in terms of memory
import sys
list1 = [0,1,2,"hellow", True]
tuple1 = (0,1,2,"hellow", True)

print(sys.getsizeof(list1), "bytes")
print(sys.getsizeof(tuple1), "bytes")

# in terms of time to create list and tuple
import timeit
# it take a statement to do and a number to repeat that task
# here i am creating a list and a tuple for 1000000 times
print(timeit.timeit(stmt="[1,2,3,4,True,6,7,8,9,0]", number=1000000))
print(timeit.timeit(stmt="(1,2,3,4,True,6,7,8,9,0)", number=1000000))






# Mutability:

# List: Lists are mutable, which means you can modify their elements after creation. You can add, remove, or change elements in a list.
# Tuple: Tuples, on the other hand, are immutable. Once you create a tuple, you cannot change its elements. You can't add, remove, or modify elements in a tuple.
# Syntax:

# List: Lists are defined using square brackets []. Example: my_list = [1, 2, 3].
# Tuple: Tuples are defined using parentheses (). Example: my_tuple = (1, 2, 3).
# Performance:

# List: Lists generally have a slightly larger memory overhead compared to tuples. This is because lists are designed to be flexible, allowing for dynamic resizing and modification.
# Tuple: Tuples are more memory-efficient than lists because of their immutability. Once a tuple is created, its size and elements cannot be changed.
# Use Cases:

# List: Use lists when you have a collection of items that may need to be modified, such as adding or removing elements. Lists are suitable for situations where you need a dynamic and mutable sequence of elements.
# Tuple: Use tuples when you have a collection of items that should remain constant throughout the program. Tuples are useful for situations where you want to ensure the integrity of the data and prevent accidental modifications.
