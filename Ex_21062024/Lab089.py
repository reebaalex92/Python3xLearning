# Unpacking a tuple
a, b, c = (1, 2, 3)

t = (1, 2, 3, 4, 5)
# tuple are immutable so not able to append
# t.append(6) # AttributeError: 'tuple' object has no attribute 'append'
new_t = t + (6,) # creates new tuple with 6 appended
print(new_t) # (1, 2, 3, 4, 5, 6)


# or another way
my_list = list(new_t)
my_list.append(7)
new_t = tuple(my_list)
print(new_t) # (1, 2, 3, 4, 5, 6, 7)

