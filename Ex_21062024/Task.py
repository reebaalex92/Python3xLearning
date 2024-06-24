# Write program to print right angle triangle using *
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


# Write a program to check given input is palindrome or not
def is_palindrome(input_str):
    if input_str == input_str[::-1]:
        print(f"{input_str} is a palindrome")
        return True
    else:
        print(f"{input_str} is not a palindrome")
        return False


input_str = input("Enter a string: ")
is_palindrome(input_str)


# Write a program to reverse a given string
def reverse_string(s):
    s = s[::-1]
    return s


s = input("Enter a string: ")
print("The given string is :", s, end="\n")
print("The reverse of string is :", reverse_string(s))


# Write a program to count the vowels and consonants in a given string
def count_vowels_consonants(input_str):
    vowels = 0
    consonants = 0
    for char in input_str:
        if char.isalpha():
            if char in "aeiouAEIOU":
                vowels = vowels + 1
            else:
                consonants = consonants + 1
    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonants}")


input_str = input("Enter a string: ")
count_vowels_consonants(input_str)

# Write a program to check if given two strings are anagrams or not
string1 = "listen"
string2 = "silent"
if sorted(string1) == sorted(string2):
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")

