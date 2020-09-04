import mysql.connector



class qry:
    def __init__(self):
        self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306,
                                                     database='parking')
        self.my_cursor = self.my_connection.cursor()

    def login(self,Vechile_number, Owner_name, ID_number, Token_number, Date):
        qry = "INSERT INTO Parking (Vechile_number,Owner_name,ID_number,Token_number,Date) VALUES (%s,%s,%s,%s,%s)"
        values = (Vechile_number, Owner_name, ID_number, Token_number, Date)
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()
        return True

    def delete(self,ID):
        qry = "DELETE FROM Parking WHERE Vechile_number = %s"
        value = (ID,)
        self.my_cursor.execute(qry, value)
        self.my_connection.commit()
        return True



    def search(self,ID_number):
        qry="SELECT * FROM Parking WHERE ID_number = %s"
        value=(ID_number,)
        self.my_cursor.execute(qry, value)
        data=self.my_cursor.fetchall()
        if len(data)>0:
            return True
        else:
            return False


    def userlogin(self,username, password):
        qry = "INSERT INTO user (username,password) VALUES (%s,%s)"
        values = (username, password)
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()
        return True


    def authentication(self,username,password):

        qry="select * from user where username=%s and password=%s"
        values = (username , password)
        self.my_cursor.execute(qry, values)

        data= self.my_cursor.fetchone()
        if len(data)>0:
            return True
        else:
            return False









