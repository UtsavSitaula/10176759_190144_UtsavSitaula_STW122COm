from tkinter import *
import mysql.connector




class Create:
    def __init__(self,root):
        self.root=root
        self.won = Tk()

        self.won.title("Welcome")
        self.won.geometry("800x400+400+200")
        self.title = Label(self.won, text="Create Account", font=("times new roman", 40, "bold"), bg="blue", fg="Black",
                      relief=GROOVE)
        self.title.pack(fill=X)

        self.title2 = Label(self.won, text="Please insert UserID and Password", font=("times new roman", 15, "bold"))

        self.title2.place(x=10, y=100)

        self.Frame4 = Frame(self.won, bd=4, relief=RIDGE, bg="black")
        self.Frame4.place(x=10, y=150, width=790, height=200)

        self.lbl_username = Label(self.Frame4, text="Username:", font=("times new roman", 20, "bold"))

        self.lbl_username.place(x=200, y=30)

        self.lbl_password = Label(self.Frame4, text="Password:", font=("times new roman", 20, "bold"))

        self.lbl_password.place(x=200, y=100)

        self.username123 = Entry(self.Frame4, font=("times new roman", 22, "bold"), fg="Black",
                               relief=GROOVE)
        self.username123.place(x=350, y=30)
        self.password123 = Entry(self.Frame4, font=("times new roman", 22, "bold"), fg="Black",
                               relief=GROOVE,show="*")
        self.password123.place(x=350, y=100)

        self.button_login = Button(self.Frame4, text="Signup", width=20, bg="BLUE",command=self.add_user)
        self.button_login.place(x=600, y=150)




        self.won.mainloop()


    def add_user(self):
        if self.username123.get()=="" or self.password123.get()=="" :
            messagebox.showerror("ERROR","Fill all the boxes")
        else:
            username= self.username123.get()
            password = self.password123.get()


            if self.save_user(username,password):
                messagebox.showinfo('Saved', "Data added sucessfully.")


    def save_user(self,username,password):
        self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306,
                                                     database='parking')
        self.my_cursor = self.my_connection.cursor()
        qry = "INSERT INTO user (username,password) VALUES (%s,%s)"
        values = (username,password)
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()
        return True






