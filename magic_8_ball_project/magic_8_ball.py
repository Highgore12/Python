import random
import os

positive_list = ["Yes", "Absolutely", "Definately"]
neutral_list = ["Maybe", "If you try your best", "You can always try"]
negative_list = ["No", "Never", "Absolutely Not", "No chance"]


chosen_answer = (random.randint(0,9))


print("What's your question?")
input("-")
os.system("cls")

print("Magic 8 ball says :")
print(random.choice(positive_list + neutral_list + negative_list))