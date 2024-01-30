#Variables for a^2, b^2 and c^2, with main calculation and appropriate responses. 
def calculate(a, b, c):
    a = a * a
    b = b * b
    c = c * c
    ab = a + b
    if ab == c:
        print("Correct")
    else:
        print("Incorrect")

#User input. 
a = int(input("Enter 1st number here : "))
b = int(input("Enter 2nd number here : "))
c = int(input("Enter 3rd number here : "))

#Final calculation. 
calculate(a, b, c)