input_sentence = input().upper()
output_sentence = ""

for letter in input_sentence:
    if letter == "A" or letter == "O" or letter == "U" or letter == "I" or letter == "Y":
        print("E")
    
    else:
        print(letter)

    output_sentence += letter