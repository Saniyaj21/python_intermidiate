import json
person = {"name":"Saniyaj", 'city':"kolkata", "isStudent":True, "languages":['python', 'js'], 'projects':{"CloudShop":'MERN stack', "studentQ": "python Django"}}

personJson = json.dumps(person, indent=3)  # dumps, s for string
print(personJson)

# writing a file of that json
with open ('./json/person.json', 'w') as file:
    json.dump(person, file)  #dump for file 

# json to python dictionary
person2 = json.loads(personJson)  # loads, s for string
print(person2)

# read json from file
with open ('./json/person.json', 'r') as file:
    fileJson = json.load(file)  #load for file 
    print("File Json ->",fileJson)
