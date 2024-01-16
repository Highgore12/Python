Number = 0

Player1 = True

while Number <=21:
    while Player1 == True:
        print("Player1")
        
        Player1_Number = int(input(" : "))
        
        if Player1_Number <= 0:
            print("Try again")
        if Player1_Number >= 4:
            print("Try again")

        if Player1_Number == 1 or Player1_Number == 2 or Player1_Number == 3:
            Number += Player1_Number
            print(Number)
            Player1 = False
    
    if Number == 21:
        if Player1 == False:
            print("Player1 Wins!")
            break
        if Player1 == True:
            print("Player2 Wins!")
            break
        
    if Number > 21:
        print("You Fail!")
        break

    while Player1 == False:
        print("Player2")
        
        Player2_Number = int(input(" : "))
        
        if Player2_Number >= 4:
            print("Try again")
        if Player2_Number <= 0:
            print("Try again")
        
        if Player2_Number == 1 or Player2_Number == 2 or Player2_Number == 3:
            Number += Player2_Number
            print(Number)
            Player1 = True

    if Number == 21:
        if Player1 == False:
            print("Player1 Wins!")
            break
        if Player1 == True:
            print("Player2 Wins!")
            break
    if Number > 21:
        print("You Fail!")
        break