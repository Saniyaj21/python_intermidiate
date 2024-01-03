# collections : Counter, namedTuple, OrderedDict, defaultdict, deque

from collections import namedtuple
from collections import Counter
a = "aaaaaabbbbccccc"  # it can be a list also

# counter stores the element with their counts as dictionary
my_counter = Counter(a)
print(my_counter)
# from here we can do all operations of dictionary

# counter methods
# if pass 1 one most-common, if pass 2 two most common
print(my_counter.most_common(2))
# counter to list
list1 = list(my_counter.elements())
print(list1)


# named tuple
Point = namedtuple('Point', "name,age")  # it will create a class named Point with name and age fields
pt = Point('Saniyaj', 23)
print(pt.name)

# deque
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.append(3)

print(d)
d.appendleft(7)
print(d)
print(d.popleft())
print(d)
print(d.pop())
print(d)
d.extend([9,0])
d.extendleft([6,80])
print(d)

d.rotate()
print(list(d))