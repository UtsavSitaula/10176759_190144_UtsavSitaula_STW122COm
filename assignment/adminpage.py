from tkinter import *
from tkinter import ttk
import mysql.connector




class Adminpage:
    def __init__(self,root):
        self.root=root
        self.win = Tk()

        self.win.title("Welcome")
        self.win.geometry("1600x1080+0+0")
        self.update_index = ""
        self.selected_row=""


        self.title = Label(self.win, text="PARKING MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="blue", fg="Black",
                      relief=GROOVE)
        self.title.pack(fill=X)

       ###########################USER DETAILS ###############################################################
        self.Frame1 = Frame(self.win, bd=4, relief=RIDGE, bg="black")
        self.Frame1.place(x=20, y=90, width=1000, height=600)
        self.title1 = Label(self.Frame1, text="All Details", font=("times new roman", 40, "bold"), bg="black",
                           fg="blue",relief=GROOVE)

        self.title1.pack(fill=X)

        scroll_x = Scrollbar(self.Frame1, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.Frame1, orient=VERTICAL)
        self.Parking_table = ttk.Treeview(self.Frame1, columns=("Vehicles Number","Owner Name", "Company ID","Token Number","Date"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Parking_table.xview)
        scroll_y.config(command=self.Parking_table.yview)
        self.Parking_table.heading("Vehicles Number", text="Vehicles Number")

        self.Parking_table.heading("Owner Name", text="Owner Name")
        self.Parking_table.heading("Company ID", text="Company ID")
        self.Parking_table.heading("Token Number", text="Token number")
        self.Parking_table.heading("Date", text="Date")

        self.Parking_table['show'] = "headings"

        self.Parking_table.pack(fill=BOTH,expand=1)
        self.show_book_tree()


        ########################################### FOR UPDATE#####################################################

        self.Frame3 = Frame(self.win, bd=4, relief=RIDGE, bg="black")
        self.Frame3.place(x=1100, y=90, width=380, height=600)

        self.title3 = Label(self.Frame3, text="Details", font=("times new roman", 22, "bold"), bg="Black",
                            fg="BLue", relief=GROOVE)

        self.title3.pack(fill=X)

        self.lbl_number = Label(self.Frame3, text="Vehicle Number:", font=("times new roman", 15, "bold"),bg="black",
                         fg="white")
        self.lbl_number.place(x=0,y=100)

        self.number_box = Entry(self.Frame3, font=("times new roman", 14, "bold"), bd=1, relief=GROOVE)

        self.number_box.place(x=150,y=100)
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

        self.lbl_searchby = Label(self.Frame3, text="Search by:", font=("times new roman", 18, "bold"), bg="black",
                               fg="blue")
        self.lbl_searchby.place(x=0, y=475)
        self.combo_search = ttk.Combobox(self.Frame3, font=("times new roman", 13, "bold"), state="readonly")

        self.combo_search["values"] = ("Token number","Company ID")
        self.combo_search.place(x=150,y=475)

        self.lbl_search = Label(self.Frame3, text="Search:", font=("times new roman", 18, "bold"), bg="black",
                                  fg="blue")
        self.lbl_search.place(x=0, y=550)
        self.search_box = Entry(self.Frame3, font=("times new roman", 14, "bold"), bd=1, relief=GROOVE)

        self.search_box.place(x=150, y=550)

        ##################################BUTTONS#######################################################

        self.button_search = Button(self.win, text="SEARCH", width=20, bg="green",command=self.search_now)
        self.button_search.place(x=780,y=700)

        self.button_update = Button(self.win, text="UPDATE", width=20, bg="BLUE",command=self.update)
        self.button_update.place(x=580, y=700)

        self.button_delete = Button(self.win, text="DELETE", width=20, bg="RED",command=self.delete_user)
        self.button_delete.place(x=780, y=750)

        self.button_save = Button(self.win, text="SAVE", width=20, bg="YELLOW",command=self.add_user)
        self.button_save.place(x=580, y=750)
        self.win.mainloop()

    def add_user(self):
        if self.number_box.get()=="" or self.owner_box=="" or self.ID_box=="" or self.token_box=="" or self.date_box=="":
            messagebox.showerror("ERROR","Fill all the boxes")
        else:
            Vechile_number = self.number_box.get()
            Owner_name = self.owner_box.get()
            ID_number = self.ID_box.get()
            Token_number = self.token_box.get()
            Date = self.date_box.get()

            if self.save_user(Vechile_number, Owner_name, ID_number, Token_number, Date):
                messagebox.showinfo('Saved', "Data added sucessfully.")
                self.show_book_tree()

    def save_user(self, Vechile_number, Owner_name, ID_number, Token_number, Date):
        self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306,
                                                     database='parking')
        self.my_cursor = self.my_connection.cursor()
        qry = "INSERT INTO Parking (Vechile_number,Owner_name,ID_number,Token_number,Date) VALUES (%s,%s,%s,%s,%s)"
        values = (Vechile_number, Owner_name, ID_number, Token_number, Date)
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()
        return True

    def show_book_tree(self):

        self.Parking_table.delete(*self.Parking_table.get_children())
        data = self.show_book()
        for i in data:
            self.Parking_table.insert("", "end",value=(i[1], i[2], i[3], i[4], i[5]))
        self.Parking_table.bind("<Double-1>", self.on_select)

    def show_book(self):
        self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306,
                                                     database='parking')
        self.my_cursor = self.my_connection.cursor()
        all_data = []
        qry = "SELECT * FROM Parking"
        self.my_cursor.execute(qry)
        all_data = self.my_cursor.fetchall()
        return all_data



    def on_select(self,event):
        selected_row=self.Parking_table.selection()[0]
        selected_index=self.Parking_table.index(selected_row)
        all_items=self.show_book()
        selected_item=all_items[selected_index]
        self.selected_row=selected_item[0]

        self.number_box.delete(0,END)
        self.number_box.insert(0,selected_item[1])
        self.owner_box.delete(0, END)
        self.owner_box.insert(0, selected_item[2])
        self.ID_box.delete(0, END)
        self.ID_box.insert(0, selected_item[3])
        self.token_box.delete(0, END)
        self.token_box.insert(0, selected_item[4])
        self.date_box.delete(0, END)
        self.date_box.insert(0, selected_item[5])





    def update_item(self,row,Vechile_number,Owner_name,ID_number,Token_number,Date):
        qry="UPDATE Parking SET Vechile_number=%s ,Owner_name =%s,ID_number =%s,Token_number =%s,Date =%s WHERE id =%s"
        values = (Vechile_number,Owner_name,ID_number,Token_number,Date,row)
        self.my_cursor.execute(qry,values)
        self.my_connection.commit()
        return True

    def update(self):


        Vechile_number = self.number_box.get()
        Owner_name = self.owner_box.get()
        ID_number = self.ID_box.get()
        Token_number = self.token_box.get()
        Date = self.date_box.get()

        if self.update_item(self.selected_row,Vechile_number, Owner_name, ID_number, Token_number,Date):
            messagebox.showinfo('Saved', "Data added sucessfully.")
            self.show_book_tree()



    def delete_user(self):
        self.ID = self.number_box.get()
        if self.ID == "":
            messagebox.showinfo('Error', 'Insert DETAILS')
        else:
            self.delete_users(self.ID)
            messagebox.showinfo('DELETE', " deleted")
            self.show_book_tree()

    def delete_users(self, id):
        self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306,
                                                     database='parking')
        self.my_cursor = self.my_connection.cursor()
        qry = "DELETE FROM Parking WHERE Vechile_number = %s"
        value = (self.ID,)
        self.my_cursor.execute(qry, value)
        self.my_connection.commit()

    def search_now(self):
        self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306,
                                                     database='parking')
        self.my_cursor = self.my_connection.cursor()
        selected = self.combo_search.get()
        sql=""

        if selected == "":
            messagebox.showerror("ERROR","please select the drop down")


        if selected == "Token number":
            sql = "SELECT * FROM Parking WHERE Token_number = %s"
        if selected == "Company ID":
            sql = "SELECT * FROM Parking WHERE ID_number = %s"

        searched = self.search_box.get()
        name = (searched,)
        varaible = self.my_cursor.execute(sql, name)
        varaible = self.my_cursor.fetchall()


        if len(varaible) != 0:
            self.Parking_table.delete(*self.Parking_table.get_children())
            for i in varaible:
                self.Parking_table.insert("", "end", value=(i[1], i[2], i[3], i[4], i[5]))
        else:
            messagebox.showerror("Error", "No data found")


































