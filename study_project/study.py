import os
def main():
    os.system("cls")
    correct_ans = 0
    homework = {}
    
    while True:
        SVHomework = input("\n\tEnter your SV homework: ")
        ENGHomework = input("\n\tEnter the respective word in ENG: ")
        
        homework[SVHomework] = ENGHomework
        
        add = input("\n\tDo you want to add more? y/n ")

        if add == "n":
            os.system("cls")
            break
        if add == "y":
            os.system("cls")

        #Test -->

    while True:
        print(f"Amount of notes = {len(homework)}")
        
        for note in homework:
            answer = input(f"\n\t {note} : ")

            if answer == homework[note]:
                print("\n\tCorrect!")
            else:
                print(f"Wrong, The corrects answer was: {homework[note]}")

        again = input("\n\tOne more time? y/n ")
        os.system("cls")
        
        if (again == "n"):
            os.system("cls")
            break


main()