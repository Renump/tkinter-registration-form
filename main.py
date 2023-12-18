from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Registration Form")
window.geometry("600x400")

lb1 = Label(window, text="Registration Form ", font=("bold", 20))
lb1.pack()

lb2 = Label(window, text="username", width=20, font=("arial", 12))
lb2.place(x=20, y=120)

entry_2 = Entry(window, width=30)
entry_2.place(x=200, y=120)

lb3 = Label(window, text="Email", width=20, font=("arial", 12))
lb3.place(x=19, y=160)

entry_3 = Entry(window, width=30)
entry_3.place(x=200, y=160)

lb4 = Label(window, text="phone Number", width=13, font=("arial", 12))
lb4.place(x=20, y=200)

entry_4 = Entry(window, width=30)
entry_4.place(x=200, y=200)

lb5 = Label(window, text="Enter Password", width=13, font=("arial", 12))
lb5.place(x=19, y=240)

entry_5 = Entry(window, show='*', width=30)
entry_5.place(x=200, y=240)


def message():
    messagebox.showinfo("congrats", "successfully registered")


Button(window, text="Register", command=message, width=10, font="bold").place(x=200, y=300)

window.mainloop()
