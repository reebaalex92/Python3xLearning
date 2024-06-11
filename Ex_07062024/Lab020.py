# In built functions
# Functions -> Repeat a task - use functions
# print() ,max(),input(),min(),type(),format(),id(),sum(),avg()
# Function related to strings
name = "Vishal"
print(name)
print(type(name))
print(id(name)) # id -gives the memory location
print(len(name)) # length of string (starts from 1)
name = name.upper()
print(name)
name = name.lower()
print(name)
name = name.casefold()
print(name)
b = name.count('v')
print(b)
c = name.find('s')
print(c)
d = name[0]
print(d)
e = name[6]  # string index out of range
print(e)
name[5] = 'a'  # strings are immutable
print(name)  # 'str' object does not support item assignment


