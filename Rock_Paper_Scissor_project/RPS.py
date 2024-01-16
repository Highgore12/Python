import random

Computer_points = 0
User_points = 0

1 == "Rock"
2 == "Paper"
3 == "Scissor"

while True:
    Computer_input = random.randint(1,3)
    User_input = int(input("User : "))

    number = User_input - Computer_input

    if number == 0:
        print("Draw!")
    
    if number == -1 or number == 2:
        print("You Lose!")
        Computer_points += 1

    if number == 1 or  number == -2:
        print("You win!")
        User_points += 1

    if User_points == 3:
        print("You Win this game!")
        break
    
    if Computer_points == 3:
        print("You Lose this game!")
        break