set1 = {10, 20, 30,  40, 50}
set2 = {30, 40, 50}
my_set = set2.issubset(set1)
print(my_set)
my_set = set1.issuperset(set2)
print(my_set)
set3 = {60, 70}
my_set = set3.issubset(set1)
print(my_set)
my_set = set1.issuperset(set3)
print(my_set)