from tkinter import *
from tkinter import messagebox
import lottery

root = Tk()
root.title("Lottery")
root.geometry("350x250")

listbox = Listbox(root, height=4, width=30, bg="white", activestyle="dotbox", font="Comfortaa", fg="blue")
lottery = lottery.Lottery()

#reward = lottery.get_reward()
#print(f'reward={reward}')

Label_amount = Label(root, text="Tickets: Max 3")
Label_amount.grid(row=0, column=0, sticky=E, padx=5, pady=5)

Textbox_amount = Entry(root, width=2)
Textbox_amount.grid(row=0, column=1, sticky=W, padx=5, pady=5)
Textbox_amount.focus_set()

def update_Listbox(Tickets):
    #print("Update_Listbox()")
    listbox.delete(0, END)
    listbox.insert(1, "Congradulations! You won: ")

    try: 
        int_amount_ticket = int(Tickets)
        i=0

        if (int_amount_ticket < 4):

            while i<int_amount_ticket:
                reward= lottery.get_reward()
                listbox.insert((i+2), reward)
                i = i+1

        else:
            messagebox.showinfo("Error. Too many tickets.")



    except ValueError:
        messagebox.showinfo("Error. Only Numbers Allowed.")

def clickRandom_numberButton():
    #print("clickRandom_numberButton()")

    amount_ticket = Textbox_amount.get()
    Textbox_amount.delete(0, END)
    Textbox_amount.focus_set()

    update_Listbox(amount_ticket)

Button_random = Button(text="Lucky Clicker", command=clickRandom_numberButton)
Button_random.grid(row=1, column=0, columnspan=2, padx=15, pady=15)

listbox.grid(row=2, column=0, columnspan=2, padx=15, pady=15)



root.mainloop()