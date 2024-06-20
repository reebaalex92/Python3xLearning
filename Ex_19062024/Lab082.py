# Double the given list
# Using for loop
my_list = [1, 2, 3, 4, 5]
temp_list = []
for i in my_list:
    temp_list.append(i*2)
print(temp_list)

# Map()
# 1. Takes each item of the list
# 2. Execute the function on it
# 3. Return the same number of elements (list)


# using lambda
my_list = [1, 2, 3, 4, 5]
temp_list = list(map(lambda i: i*2, my_list))
print(temp_list)

# using function
def double(x):
    return x*2
my_list = [1, 2, 3, 4, 5]
temp_list = list(map(double, my_list))
print(temp_list)