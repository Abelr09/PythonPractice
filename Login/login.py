from tkinter import *
from tkinter import messagebox


def login():
    username = entry1.get()
    password = entry2.get()

    if username == "" and password == "":
        messagebox.showinfo("", "Blanck not allowed")

    elif username == "Abel" and password == "admin":
        messagebox.showinfo("", "Login succesfully!")

    else:
        messagebox.showinfo("", "Incorrect username and password")


root = Tk()
root.title("Login")
root.geometry("400x300+500+50")
global entry1
global entry2

Label(root, text="Username").place(x=20, y=20)
Label(root, text="Password").place(x=20, y=70)

entry1 = Entry(root, bd=5)
entry1.place(x=140, y=20)

entry2 = Entry(root, bd=5)
entry2.place(x=140, y=70)

Button(root, text="Login", command=login, height=3, width=13, bd=8).place(x=150, y=120)


root.mainloop()
