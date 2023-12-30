# List Initialization:
# Create an empty list called my_list. Add three different types of elements to it: an integer, a string, and a float.

my_list = [90, "saniyaj", 90.88]


# List Slicing:
# Given the list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9], create a new list containing only the even numbers using list slicing.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = numbers[1::2]
print(new_list)


# List Append and Extend:
# Create two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6]. Use both append and extend methods to combine them into a single list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# method 1
# list1.append(list2)

# method 2
list1.extend(list2)
print(list1)


# List Insert and Remove:
# Start with a list of fruits: fruits = ['apple', 'banana', 'orange']. Insert 'grape' at the second position and then remove 'banana'.
fruits = ['apple', 'banana', 'orange']
fruits.insert(1, "grape")
fruits.remove("banana")
print(fruits)


# List Indexing and Count:
# Given the list colors = ['red', 'blue', 'green', 'red', 'yellow'],
#  find the index of the first occurrence of 'red' and count how many times 'red' appears in the list.
colors = ['red', 'blue', 'green', 'red', 'yellow']
print(colors.index("red"))
print(colors.count("red"))


# List Sorting and Reversing:
# Create a list of numbers in random order. Sort the list in ascending order and then reverse the order.
nums = [5, 3, 5, 73, 3, 6, 8, 36, 3, 3, 5]
nums.sort()  # directly mutate the original list
print(nums)
nums.reverse()  # directly mutate the original list
print(nums)


# List Comprehension:
# Generate a list of squares for the numbers from 1 to 10 using list comprehension.
s_list = [i*i for i in range(1, 11)]
print(s_list)


# List Copying:
# Create a list called original_list with some elements.
#  Create a new list called copied_list and copy the elements from original_list using both the copy method and the slicing method.
original_list = [90, 80, 70, 60, 50, 40]
copied_list_1 = original_list.copy()
copied_list_2 = original_list[::1]
print(copied_list_1)
print(copied_list_2)

# List Pop and Index:
# Start with a list of characters: characters = ['a', 'b', 'c', 'd', 'e'].
#  Use the pop method to remove the third element and then find the index of 'd'.
characters = ['a', 'b', 'c', 'd', 'e']
characters.pop(2)
print(characters.index("d"))
print(characters)


# List Concatenation:
# Given two lists, list_a = [1, 2, 3] and list_b = [4, 5, 6], concatenate them to create a new list called result_list.
list_a = [1, 2, 3]
list_b = [4, 5, 6]
result_list = list_a+list_b
print(result_list)
