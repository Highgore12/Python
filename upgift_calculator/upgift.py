def main():

    print("Type 1 for addition or 2 for subtraction")
    meth = int(input(": "))

    x = int(input("What's X? "))
    y = int(input("What's Y? "))

    if meth > 1:
        print("The answer is", x - y)
    
    else: 
        print("The answer is", x + y)

main()