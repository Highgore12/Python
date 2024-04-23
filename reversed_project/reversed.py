result_Back = ""
while True:
    word = input("Word : ").lower()

    if len(word) >= 2:

        for Back in reversed(word):
            result_Back += Back

        if result_Back == word:
            print("This IS a Palindrome")
            break
        
        else:
            print("This IS NOT a Palindrome")
            break
        
    else:
        print("Please input 2 or more letters.")