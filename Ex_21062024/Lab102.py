my_dict = dict()
my_dict['a'] = 10
my_dict['c'] = 100
my_dict['b'] = 1000
my_dict['e'] = 10000
my_dict['d'] = 100000
my_dict['f'] = 1000000
print(my_dict)

for key, value in my_dict.items():
    print(key, value)
# normally dictionary not keep the order of insertion so to make it order we use OrderedDict.
