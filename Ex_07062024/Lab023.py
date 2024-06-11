# List
# Shopping list
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])
# list of different data types
mixed_list = ["milk", "pasta", 1, 3.14, True]
print(mixed_list)
print(type(mixed_list))  # <class 'list'>
shopping_list.append("cookies")  # Add to the end of the list
print(shopping_list)
shopping_list.insert(1, "chocolate")  # Add to the beginning of the list
print(shopping_list)
shopping_list.extend(["cookies", "chocolate"])  # Add multiple items to the end of the list
print(shopping_list)
shopping_list.remove("cookies")  # Remove an item from the list
print(shopping_list)
shopping_list.pop()  # Remove the last item from the list
print(shopping_list)
shopping_list.index("eggs")  # Gives the index of the item
print(shopping_list)
shopping_list.sort()  # Sort the list
print(shopping_list)
shopping_list.reverse()  # Reverse the list
print(shopping_list)
shopping_list[0] = "sauce"  # Change the value of an item
print(shopping_list)


