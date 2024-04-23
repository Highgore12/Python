dictionary = {}

word = input("Enter here : ").upper()

for letter in word:
    if letter in dictionary:
        dictionary[letter] += 1
    else:
        dictionary[letter] = 1

print(dictionary)