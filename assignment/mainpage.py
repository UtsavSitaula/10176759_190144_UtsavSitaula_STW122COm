from tkinter import *
import tkinter.messagebox

import random
import datetime
from assignment.adminlogin import Admin
from assignment.user import User
from assignment.guest import Guest




class Main:
    def __init__(self,root):
        self.root=root
        self.root.title("Welcome")
        self.root.geometry("800x400+400+200")
        title = Label(self.root, text="WELCOME", font=("times new roman", 40, "bold"), bg="blue", fg="Black",
                      relief=GROOVE)
        title.pack(side=TOP, fill=X)
        button_guest= Button(self.root, text="Log in as Guest",font=("times new roman",25,"bold"), width=40, bg="blue",command=self.Guestimport)
        button_guest.place(x=150, y=100, width=500, height=60)
        button_admin = Button(self.root, text="Log in as Admin", font=("times new roman", 25, "bold"), width=40,
                              bg="blue",command=self.change)
        button_admin.place(x=150, y=200, width=500, height=60)
        button_user = Button(self.root, text="Log in as User", font=("times new roman", 25, "bold"), width=40,
                              bg="blue",command=self.userchange)
        button_user.place(x=150, y=300, width=500, height=60)
        button_exit = Button(self.root, text="EXIT", font=("times new roman", 25, "bold"), width=40,
                             bg="red",command=exit)
        button_exit.place(x=675, y=300, width=100, height=60)


    def change(self):
        Admin(self.root)

    def userchange(self):
        User(self.root)

    def Guestimport(self):
        Guest(self.root)




root=Tk()
oc=Main(root)
root.mainloop()

