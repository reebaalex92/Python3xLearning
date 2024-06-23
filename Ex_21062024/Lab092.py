t = ("TheTestingAcademy", "python", "Academy", "TheTestingAcademy")
print(set(t))
print(len(set(t)))

set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}
my_set = set1.union(set2)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.intersection(set2)
print(my_set)

my_set = set1.difference(set2)
print(my_set)
my_set = set2.difference(set1)
print(my_set)


