# List of numbers
numbers = [1, 2, 3, 4, 5]

# Indexing
print(numbers[0])  # Output: 1

# Changing an element
numbers[2] = 90
print(numbers)  # Output: [1, 2, 90, 4, 5]

# Appending an element
numbers.append(6)
print(numbers)  # Output: [1, 2, 90, 4, 5, 6]

# Extending a list
numbers.extend([7, 8, 9])
print(numbers)  # Output: [1, 2, 90, 4, 5, 6, 7, 8, 9]

# Inserting an element
numbers.insert(3, 'b')
print(numbers)  # Output: [1, 2, 90, 70, 4, 5, 6, 7, 8, 9]

# Removing an element
numbers.remove('b')
print(numbers)  # Output: [1, 2, 90, 4, 5, 6, 7, 8, 9]

# Copy a list
new_list = numbers.copy()
print(new_list)  # Output: [1, 2, 90, 4, 5, 6, 7, 8, 9]

# Clear a list
numbers.clear()
print(numbers)  # Output: []

# Sort ing a list
new_list.sort()
print(new_list)  # Output: [1, 2, 4, 5, 6, 7, 8, 9, 90]

# Reverse a list
new_list.reverse()
print(new_list)  # Output: [90, 9, 8, 7, 6, 5, 4, 2, 1]

print(new_list[0])
print(new_list[1])
print(new_list[2])
print(new_list[3])
