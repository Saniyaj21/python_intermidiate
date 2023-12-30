myList = [2, 3, 44,]

l2 = list()
print(l2)
l2.append("L2")

# get values
for i in myList:
    print(i)
for i in range(len(myList)):
    print(myList[i])

# check member or not
if 2 in myList:
    print(True)

# inserting the element
myList.append("sani")  # insert al the end of the loat
myList.insert(1, "Shubha")  # inser a 1 index

# deleteting element
print("Before pop", myList)
res = myList.pop()  # return the last element
print(res)

myList.remove(2)  # specic element to remove
myList.clear()  # remove all

mylist7 = [1,1,3]
print(mylist7.index(1)) 

myList.reverse()
myList.sort()  # it change the original list
# did not change a list but create a sorted copy of it
newList = sorted(myList)

l3 = [2] * 5
print(l3)

l4 = l3+l2
print(l4)

# slicing
print(l4[2:4])
print(l4[::-1])

# coping a list

# copy by memory reference 
lOrg = ["sani", "Shubha", "papu"]

newCopy = lOrg

print(newCopy)
newCopy.append("MUTING LIST") # also modified th original list
print(lOrg)

# coping by value
o2 = [6]*4

# both create a copy of original list
n2 = o2.copy()
n3 = list(o2)
n2.pop()
print("o2",o2)
print("n2",n2)


# list comprehension
com = [1,2,3,4,5]
listCompre = [i+i for i in com]
print(com)
listCompre.append(8)
print(listCompre)

print("end print", myList)
