from tkinter import *
import mysql.connector




class Guest:
    def __init__(self,root):
        self.root=root
        self.win = Tk()

        self.win.title("Welcome")
        self.win.geometry("1000x700+300+50")
        self.update_index = ""
        self.title = Label(self.win, text="Welcome Guest", font=("times new roman", 40, "bold"), bg="blue", fg="Black",
                      relief=GROOVE)
        self.title.pack(fill=X)




        self.Frame3 = Frame(self.win, bd=4, relief=RIDGE, bg="black")
        self.Frame3.place(x=10, y=90, width=380, height=600)

        self.title2 = Label(self.Frame3, text="NOTE: For Guest Token Number must be filled",
                            font=("times new roman", 12, "bold"), bg="black", fg="white",
                            relief=GROOVE)
        self.title2.place(x=10,y= 550)

        self.title3 = Label(self.Frame3, text="Details", font=("times new roman", 22, "bold"), bg="Black",
                            fg="BLue", relief=GROOVE)

        self.title3.pack(fill=X)

        self.lbl_number = Label(self.Frame3, text="Vehicle Number:", font=("times new roman", 15, "bold"), bg="black",
                                fg="white")
        self.lbl_number.place(x=0, y=100)

        self.number_box = Entry(self.Frame3, font=("times new roman", 14, "bold"), bd=1, relief=GROOVE)

        self.number_box.place(x=150, y=100)
        self.lbl_owner = Label(self.Frame3, text="Owner Name:", font=("times new roman", 15, "bold"), bg="black",
                               fg="white")
        self.lbl_owner.place(x=0, y=175)
        self.owner_box = Entry(self.Frame3, font=("times new roman", 14, "bold"), bd=1, relief=GROOVE)

        self.owner_box.place(x=150, y=175)
        self.lbl_ID = Label(self.Frame3, text="Company ID:", font=("times new roman", 15, "bold"), bg="black",
                            fg="white")
        self.lbl_ID.place(x=0, y=250)
        self.ID_box = Entry(self.Frame3, font=("times new roman", 14, "bold"), bd=1, relief=GROOVE)

        self.ID_box.place(x=150, y=250)
        self.lbl_token = Label(self.Frame3, text="Token Number:", font=("times new roman", 15, "bold"), bg="black",
                               fg="white")
        self.lbl_token.place(x=0, y=325)
        self.token_box = Entry(self.Frame3, font=("times new roman", 14, "bold"), bd=1, relief=GROOVE)

        self.token_box.place(x=150, y=325)
        self.lbl_date = Label(self.Frame3, text="Date:", font=("times new roman", 15, "bold"), bg="black",
                              fg="white")
        self.lbl_date.place(x=0, y=400)
        self.date_box = Entry(self.Frame3, font=("times new roman", 14, "bold"), bd=1, relief=GROOVE)

        self.date_box.place(x=150, y=400)

        self.button_search = Button(self.Frame3, text="SAVE", width=20, bg="green",command=self.add_user)
        self.button_search.place(x=170, y=475)

        self.Frame1 = Frame(self.win, bd=4, relief=RIDGE, bg="black")
        self.Frame1.place(x=400, y=90, width=550, height=600)

        scroll_x = Scrollbar(self.Frame1, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.Frame1, orient=VERTICAL)
        self.Parking_table = ttk.Treeview(self.Frame1, columns=("Vehicles Number", "Owner Name","Company ID","Token Number", "Date"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Parking_table.xview)
        scroll_y.config(command=self.Parking_table.yview)
        self.Parking_table.heading("Vehicles Number", text="Vehicles Number")

        self.Parking_table.heading("Owner Name", text="Owner Name")
        self.Parking_table.heading("Company ID", text="Company ID")
        self.Parking_table.heading("Token Number", text="Token Number")
        self.Parking_table.heading("Date", text="Date")

        self.Parking_table['show'] = "headings"

        self.Parking_table.pack(fill=BOTH, expand=1)
        self.show_book_tree()

        self.win.mainloop()

    def add_user(self):
        if self.number_box.get()=="" or self.owner_box.get()==""  or self.token_box.get()=="" or self.date_box.get()=="":
            messagebox.showerror("ERROR","Fill all the boxes")
        else:
            Vechile_number= self.number_box.get()
            Owner_name = self.owner_box.get()
            ID_number = self.ID_box.get()
            Token_number= self.token_box.get()
            Date = self.date_box.get()


            if self.save_user(Vechile_number,Owner_name,ID_number,Token_number,Date):
                messagebox.showinfo('Saved', "Data added sucessfully.")
                self.show_book_tree()

    def save_user(self,Vechile_number,Owner_name,ID_number,Token_number,Date):
        self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306,
                                                     database='parking')
        self.my_cursor = self.my_connection.cursor()
        qry = "INSERT INTO parking (Vechile_number,Owner_name,ID_number,Token_number,Date) VALUES (%s,%s,%s,%s,%s)"
        values = (Vechile_number,Owner_name,ID_number,Token_number,Date)
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()
        return True

    def show_book_tree(self):

        self.Parking_table.delete(*self.Parking_table.get_children())
        data = self.show_book()
        for i in data:
            self.Parking_table.insert("", "end", value=(i[1], i[2], i[3], i[4], i[5]))

    def show_book(self):
        self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306,
                                                     database='parking')
        self.my_cursor = self.my_connection.cursor()
        all_books = []
        qry = "SELECT * FROM parking"
        self.my_cursor.execute(qry)
        all_books = self.my_cursor.fetchall()
        return all_books


