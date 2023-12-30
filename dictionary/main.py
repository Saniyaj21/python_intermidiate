myDict = {"name": "Saniyaj", "AGE": 22}
print(myDict)

mydict2 = dict(name="shubha", age=22)
print(mydict2)

# access values
v = mydict2["age"]
print(v)

# keys are case sensitive
# print(myDict["age"])  # give error because -> age != AGE

# inserting values

# mydict2["key"] = "Value"
mydict2["college"] = "Haldia Institute of Technology"
print(mydict2)

# deleting elements
del mydict2["college"]
print(mydict2)

# 2nd way
mydict2.pop("age")
print(mydict2)

# 3rd way
# it removes the last item in a dictionary
mydict2.popitem()
print(mydict2)


# checking key is in dict or not
if "AGE" in myDict:
    print(True)

# loops
print("\n")
for key in myDict:
    print(key)

for key in myDict.keys():
    print(key)
    
for value in myDict.values():
    print(value)

for key, value in myDict.items():
    print(key," : ",value)

# coping
    
# pass by reference
copy = myDict
print(myDict)
copy["college"] = "HIT"
print(myDict)

# pass by value
copy2 = myDict.copy()
# or
copy3 = dict(myDict)

print(myDict)
copy2["dob"] = "2001"
print(myDict)

# update method
dt_1 = {"name":"saniya", "lastname":"mallik", "city":"HALDIA"}
dt_2 = dict(name = "Shubha", lastname = "Manna", email="shubha@gmail.com")

# takes the upadted value for same keys and take rest keys as it is  
dt_1.update(dt_2)
print(dt_1)















