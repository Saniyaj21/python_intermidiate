# Dictionary Initialization:

# Create an empty dictionary called my_dict. Add three key-value pairs to it, where the keys are strings and the values are integers.
my_dict = {"age": 22, "roll": 1, "year": 1}


# Access and Modify:

# Given the dictionary student = {'name': 'John', 'age': 20, 'grade': 'A'}, change John's age to 21 and update his grade to 'B'.
student = {'name': 'John', 'age': 20, 'grade': 'A'}
student["age"] = 21
student["grade"] = "B"

print(student)


# Keys and Values:

# Create a dictionary representing a book with 'title', 'author', and 'year' as keys. Print all the keys and values separately.
book = {"title": "Human Anatomy", "year": 2023,
        "auther": "Dr. Ashvini Kumar Dwivedi"}
print(book.keys())
print(book.values())

for key in book:
    print("key ", key)
    print("value ", book[key])

for key, value in book.items():
    print(key, ":", value)


# Dictionary Update:

# Merge two dictionaries: dict1 = {'a': 1, 'b': 2} and dict2 = {'b': 3, 'c': 4}. Use a dictionary method to update dict1 with values from dict2.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)  # directly mutate dictionary
print(dict1)


# Dictionary Pop and Popitem:

# Given the dictionary colors = {'red': 1, 'blue': 2, 'green': 3}, use pop to remove 'blue' and use popitem to remove any key-value pair.
colors = {'red': 1, 'blue': 2, 'green': 3}
colors.pop("blue")
colors.popitem() #pop from right of dictionary

print(colors)

# Dictionary Copy:

# Create a dictionary called original_dict. Create a shallow copy named copied_dict and modify a value in copied_dict without changing the original.
original = {"name":"Sani"}

# copy_original = dict(original)
copy_original = original.copy()

copy_original["age"] =22

print(original)
print(copy_original)


# Dictionary Comprehension:

# Generate a dictionary containing squares for the numbers from 1 to 5 using dictionary comprehension.
squares_dict = {num: num**2 for num in range(1, 6)}
print(squares_dict)

# Key Existence Check:

# Check if the key 'country' exists in the dictionary person_info = {'name': 'Alice', 'age': 25, 'gender': 'Female'}.
# If it does, print its value; otherwise, print a default message.
person_info = {'name': 'Alice', 'age': 25, 'gender': 'Female'}
if 'country' in person_info:
    print(person_info['country'])
else:
    print("Country is not present in the List")


# Dictionary Values to List:

# Given a dictionary of temperatures temperatures = {'Monday': 30, 'Tuesday': 25, 'Wednesday': 28}, create a list containing all the temperatures.
temperatures = {'Monday': 30, 'Tuesday': 25, 'Wednesday': 28}
my_list = [temperatures[i] for i in temperatures]
# my_list = list(temperatures.values())
print(my_list)

# Nested Dictionary:

# Create a nested dictionary representing information about a student, including 'personal' and 'academic' information. Print some details using nested indexing.
# Create a nested dictionary representing information about a student
student_info = {
    'personal': {
        'name': 'John Doe',
        'age': 20,
        'gender': 'Male'
    },
    'academic': {
        'major': 'Computer Science',
        'grade': 'A',
        'courses': ['Python Programming', 'Data Structures']
    }
}

# Print some details using nested indexing
print("Student's name:", student_info['personal']['name'])
print("Student's age:", student_info['personal']['age'])
print("Major:", student_info['academic']['major'])
print("Courses:", student_info['academic']['courses'])
