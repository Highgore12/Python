import random

print("\n------------------------------------------\n")
print(".:Guessing Game:.\n")
print("Guess a number between 1-10, you get 3 tries\n")

randomnumber = random.randint(1, 10)
print(randomnumber)
i=0
found = False


while i<3:
    guessed = input("Make your guess: ")
    
    if randomnumber == int(guessed):
        found = True
        print ("Congratulations! You won!")
        break

    i += 1

    if found:
        print("*")
    
    else:
        print("WRONG! Try again.")

print("-------------------------------------")