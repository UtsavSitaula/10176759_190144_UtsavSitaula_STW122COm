from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import datetime
from assignment.adminpage import Adminpage

class Admin:
    def __init__(self, root):
        self.root = root
        self.win = Tk()

        self.win.title("Welcome")
        self.win.geometry("800x400+400+200")
        self.title = Label(self.win, text="Welcome admin", font=("times new roman", 40, "bold"), bg="blue", fg="Black",
                           relief=GROOVE)
        self.title.pack(fill=X)

        self.title2 = Label(self.win, text="Please insert UserID and Password", font=("times new roman", 15, "bold"))

        self.title2.place(x=10, y=100)

        self.Frame4 = Frame(self.win, bd=4, relief=RIDGE, bg="black")
        self.Frame4.place(x=10, y=150, width=790, height=200)

        self.lbl_username = Label(self.Frame4, text="Username:", font=("times new roman", 20, "bold"))

        self.lbl_username.place(x=200, y=30)

        self.username1 = Entry(self.Frame4, font=("times new roman", 22, "bold"), fg="Black",
                               relief=GROOVE)
        self.username1.place(x=350, y=30)

        self.lbl_password = Label(self.Frame4, text="Password:", font=("times new roman", 20, "bold"))

        self.lbl_password.place(x=200, y=100)


        self.password1 = Entry(self.Frame4, font=("times new roman", 22, "bold"), fg="Black",
                               relief=GROOVE,show="*")
        self.password1.place(x=350, y=100)

        self.button_login = Button(self.Frame4, text="Log In", width=20, bg="BLUE",command=self.send)
        self.button_login.place(x=600, y=150)

        self.win.mainloop()

    def goto(self):
        Adminpage(self.root)



    def send(self):
        x= self.username1.get()
        y= self.password1.get()
        if x=="admin":
            if y=="admin":
                self.win.destroy()
                self.goto()
            else:
                pass
        else:
            messagebox.showerror("ERROR","WRONG ID PASSWORD")







