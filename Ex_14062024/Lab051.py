# break -> based on condition it will break the loop
# pass -> do nothing or skip the loop
for i in range(11): # Mentions 0-10
    print(i)
print('\n')
for i in range(11):
    if i == 5: # skip 5 and go back to loop
        pass
    else:
        print(i)
print('\n')
for i in range(11):
    if i == 5 or i == 6: # skip 5 and 6 go back to loop
        pass
    else:
        print(i)
