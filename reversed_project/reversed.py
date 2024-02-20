result_Back = ""
result_For = ""

#Input
word = input("Word : ").lower()

#Calculation Backwards
for Back in reversed(word):
    result_Back += Back

#Calculation Forwards
for For in (word):
    result_For += For

#Results
if result_For == result_Back:
    print("This IS a Palindrome")
else:
    print("This IS NOT a Palindrome")