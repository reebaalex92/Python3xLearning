def print_argument(*args):
    for i in args:
        print(i, end="\n")


print_argument(1, 2, 3, 4, 5)

# Same program can be written as below
# *args -> list
a = [1, 2, 3, 4, 5]
for i in a:
    print(i, end=" ")
print("\n")
for i in range(1, 10):
    print(i, end="\n")
