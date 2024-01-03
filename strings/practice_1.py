# String Concatenation:

# Create two strings, one containing your first name and the other containing your last name. Concatenate them to form your full name.
first_name = "Saniyaj"
last_name = "Mallik"

print(first_name + last_name)


# String Indexing and Slicing:

# Given the string 'Python is powerful', print the first three characters, the last four characters, and a substring containing 'is'.
python = 'Python is powerful'
print(python[:4])
print(python[-4:])
index = python.index('i')
print(python[index:index+2])


# String Length:

# Find and print the length of the string 'Hello, World!'.
str_1 = 'Hello, World!'
print(len(str_1))

# String Formatting:

# Use string formatting to create a sentence that includes a variable for your age. For example, "I am 25 years old."
age = 21
me = f"I am {age} years old."
print(me)

# String Methods - Uppercase and Lowercase:

# Given a string, convert it to uppercase and then to lowercase. Print both versions.
print(me.upper())
print(me.lower())

# String Replace:

# Replace all occurrences of the word 'apple' with 'orange' in the string 'I have an apple, and she has an apple too.'.
str_2 = 'I have an apple, and she has an apple too.'
str_3 = str_2.replace("apple", "orange")
print(str_3)

# String Splitting:

# Split the string 'Python,Java,JavaScript' into a list of programming languages using the split method.
str_4 = 'Python,Java,JavaScript'
lt = str_4.split(',')
print(lt)


# String Joining:

# Given a list of words ['I', 'love', 'Python'], join them into a single string using a space as the separator.
lt1 = ['I', 'love', 'Python']
str_5= " ".join(lt1)
print(str_5)


# String Count:

# Count the number of occurrences of the letter 'a' in the string 'banana'.
str_6 = 'banana'
print(str_6.count('a'))


# String Stripping:

# Given the string ' Python is fun ', remove the leading and trailing whitespaces.
str_7 = ' Python is fun '
print(str_7.strip())
