reebadetails = {
    "name": "Reeba",
    "isFemale": True,
    "age": 13,
    "address": "Mumbai"

}
print(reebadetails)
print(reebadetails["name"])
print(reebadetails.get("name"))
print(reebadetails.values())
print(reebadetails.keys())
print(reebadetails.items())


my_dict = {'a': 1, 'b': 30, 'c': 10, 'a': 100 } # values can be duplicate but keys can't
print(my_dict)
print(len(my_dict))
print(list(my_dict.keys()))
print(list(my_dict.values()))
for i in list(my_dict.keys()):
    print(i)


for i in list(my_dict.values()):
    print(i)

for key, value in my_dict.items():
    print(key, value)