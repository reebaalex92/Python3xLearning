# For Loop
print('The even numbers')
for counter in range(0, 101, 2): # prints the even numbers
    print(counter)
print('The odd numbers')
for counter in range(1, 100, 2): # prints the odd numbers
    print(counter)

for counter in range(1,101) : # prints the numbers from 1 to 100
    print(counter)
    if counter == 10 :
        break

print("Outside of the program")