# lambda arguments : expression
def add(x): return x+10


print(add(3))


def sumTwo(x, y): return x+y


print(sumTwo(4, 5))

points = [(1, 2), (15, 1), (5, -1), (10, 4)]
points_sorted = sorted(points) # sort by the first element
points_sorted2 = sorted(points, key = lambda x:x[1]) # giving the key to sort by the 2nd element
print(points)
print(points_sorted)
print(points_sorted2)


# map function
list1 = [1,2,3,4,5]
result = map(lambda x: x+x, list1)
print(list(result))

# filter function
list2 = [1,2,3,4,5,6]
result2 = filter(lambda x: x%2 == 0, list2)
print(list(result2))

# reduce function
from functools import reduce
list2 = [1,2,3,4,5,6]
result3 = reduce(lambda x, y: x*y, list2)
print(result3)



