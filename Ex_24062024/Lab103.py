# To find key in dictionary
test_dict = {'gfg': 1, 'is': 2, 'a': 3}

for k,  v in test_dict.items():
    if k == 'a':
        print("Yes")


op = 'a' in test_dict
print(op)
