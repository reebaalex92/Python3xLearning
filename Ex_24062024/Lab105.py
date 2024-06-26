# Filter the vowels

letters = ['a', 'b', 'c', 'd', 'e', 'i', 'o', 'j', 'k', 'm', 'n']


def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels


filtered_vowels = filter(filter_vowels, letters)
print('The filtered vowels are:', list(filtered_vowels))
