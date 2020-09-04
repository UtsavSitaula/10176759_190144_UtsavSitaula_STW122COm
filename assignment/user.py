from tkinter import *
from assignment.createaccount import Create
from assignment.userdetails import Details
import mysql.connector



class User:
    def __init__(self,root):
        self.root=root
        self.wan = Tk()

        self.wan.title("Welcome")
        self.wan.geometry("800x600+400+100")
        self.title = Label(self.wan, text="Welcome User", font=("times new roman", 40, "bold"), bg="blue", fg="Black",
                      relief=GROOVE)
        self.title.pack(fill=X)
        self.title2 = Label(self.wan, text="Please insert you ID and Password:", font=("times new roman",15, "bold"))

        self.title2.place(x=10,y=100)

        self.Frame6 = Frame(self.wan, bd=4, relief=RIDGE, bg="black")
        self.Frame6.place(x=10, y=150, width=790, height=200)

        self.lbl_username = Label(self.Frame6, text="Username:", font=("times new roman", 20, "bold"))

        self.lbl_username.place(x=200, y=30)

        self.lbl_password = Label(self.Frame6, text="Password:", font=("times new roman", 20, "bold"))

        self.lbl_password.place(x=200, y=100)

        self.username12 = Entry(self.Frame6, font=("times new roman", 22, "bold"), fg="Black",
                               relief=GROOVE)
        self.username12.place(x=350, y=30)
        self.password12 = Entry(self.Frame6, font=("times new roman", 22, "bold"), fg="Black",
                               relief=GROOVE,show="*")
        self.password12.place(x=350, y=100)

        self.button_login= Button(self.Frame6, text="LOGIN", width=20, bg="BLUE",command=self.login)
        self.button_login.place(x=600, y=150)

        self.title3 = Label(self.wan, text="Don't have a account. Create Account", font=("times new roman", 15, "bold"))

        self.title3.place(x=10, y=350)

        self.button_create = Button(self.wan, text="Create a Account", font=("times new roman", 12, "bold"), width=40,
                                  bg="Green",command=self.go)
        self.button_create.place(x=350, y=370, width=300, height=40)

        self.wan.mainloop()

    def go(self):
        Create(self.root)

    def send(self):
        Details(self.root)

    def login(self):
        if self.username12.get()=="" or self.password12.get()=="":
            messagebox.showerror("ERROR","fill all the areas")
        else:
            try:
                self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306,
                                                             database='parking')
                self.my_cursor = self.my_connection.cursor()
                self.my_cursor.execute("select * from user where username=%s and password=%s",(self.username12.get(),self.password12.get()))
                row=self.my_cursor.fetchone()
                if row==None:
                    Messagebox.showerror("ERROR","INVALID username or password")
                else:
                    messagebox.showinfo("SUCESS","WELCOME")
                    self.wan.destroy()
                    self.send()



            except:
                messagebox.showerror("ERROR","ERROR")















