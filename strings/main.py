
# Strings are ordered, immutable, text representation

name = "saniyaj"
name2 = 'sani'
name3 = '''
name ->
saniyaj
'''
# name[2] = "j"  #error strings are immutable

# all slicing works here also
# all loops works here also

# name will lost reference of "saniyaj" and a new reference will be created
name = name + name2
print(name)

if 's' in name:
    print("yes")

# methods
text = "    Sani Mallik"
print(text.strip()) #remove before and after white spaces
print(text.upper()) 
print(text.lower()) 
print(text.startswith(' ')) #return True
print(text.startswith('S')) #return False
print(text.endswith('Mallik')) 
print(text.find('a')) #return index of a first apperes
print(text.count('a'))
text2 = text.replace('a', "*") 
print(text2)

text = "Hi I am Saniyaj Mallik"
# string to list
myList = text.split(" ")
print(myList)

# list to string
myString = ' '.join(myList) # replace the space to join by anything like "and"
print(myString)

# string formating
name = "Sani"
# my_str = "Hi %s" %name # for string -> %s, number -> %d, floating -> %f etc
# my_str = "Hi {}".format(name)
my_str = f"Hi {name}" #python 3.6
print(my_str)












