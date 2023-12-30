# set unordered, mutable, no duplicates

set_1 = {1, 2, 3, 3, 4}
print(set_1)

set_2 = set([1, 2, 3, 4, 4, 4])
set_3 = set("Saniyaj")
print(set_3)  # order is arbitory

# inserting and deleting
set_1.add(90)
set_1.remove(2)
# if we try to remove a non existing value it will give an error
# it try to remove but if not found that element dont give any error
set_1.discard(44)

# set_1.clear()

print(set_1)
set_1.pop()


print(set_1)

# loops
# all loops and membership function can be done

# union and intersections

odds = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(even).union(primes)
print(u)

i = odds.intersection(primes)
print(i)

# difference
diff = odds.difference(primes)   # here elements present in odds but not in primes
diff2 = primes.difference(odds) # here elements present in primes but not in odds
print(diff, diff2)

# update method updates the originaal set

# odds.update(even)  #take every element in a set 
# odds.intersection_update(even)  # take the intersection of two sets
# odds.difference_update(even)  #akes element that is not present in second set
print(odds)

print(odds.issubset(primes))
print(odds.issuperset(primes))
print(odds.isdisjoint(primes))


# copies of set

setA = {1,2,3, 4,5}

# pass by reference
# setB = setA
# setB.add(8)
# print(setA)

# pass by value
setB = setA.copy()
setB = set(setA)