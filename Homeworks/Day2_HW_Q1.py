# Create a list to work on
list1 = [2,4,2,6,26,34,6,-7]

# Swap the second half the list with the first one
# First split the list
middle_index = len(list1)//2

# Swap both parts of the list
list1 = list1[middle_index :] + list1[: middle_index]
print(list1)