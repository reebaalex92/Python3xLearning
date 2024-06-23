set1 = {"TheTestingAcademy", "python", "Academy", "TheTestingAcademy"}
print(set1)
print(len(set1))
for i in set1:
    print(i)

set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])
print(set1)
print(len(set1))
set1.remove(7)
print(set1)
print(len(set1))
set1.add(120)
print(set1)
set1.pop()
print(set1) # generally removes the first item

