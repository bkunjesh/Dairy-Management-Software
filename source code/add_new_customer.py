from tkinter import *
import tkinter.messagebox
import sqlite3
import db


class Database:
    def __init__(self, master, *args, **kwargs):
        
        self.master = master
        self.conn = db.make_connection()
        self.c = self.conn.cursor()

        # heading
        self.heading = Label(self.master, text="ADD NEW CUSTOMER", font="arial 30 bold")
        self.heading.place(x=440, y=10)

        self.define_fields()

        # add new or update existing data btn
        self.btn_add_new = Button(self.master, text="Add New", width=20,height=2,font="arial 9 bold",bg="orange",fg="white",command=self.add_new_customer)
        self.btn_add_new.place(x=500, y=100)

        self.btn_update_existing = Button(self.master, text="Update", width=20,height=2,font="arial 9 bold",bg="orange",fg="white",command=self.update_existing)
        self.btn_update_existing.place(x=655, y=100)

        
    def define_fields(self,*args,**kwargs):
        self.name_l = Label(self.master, text="Name", font="arial 25 bold")        
        self.name_e = Entry(self.master, width=20, font="arial 20 bold")

        self.address_l = Label(self.master, text="Address", font="arial 25 bold")
        self.address_e = Entry(self.master, width=20, font="arial 20 bold")

        self.phone_l = Label(self.master, text="Phone Number", font="arial 25 bold")
        self.phone_e = Entry(self.master, width=20, font="arial 20 bold")

        self.reg_mor_quantity_l = Label(self.master, text="Regular Morning Quantity", font="arial 25 bold")
        self.reg_mor_quantity_e = Entry(self.master, width=20, font="arial 20 bold")

        self.reg_mor_rate_l = Label(self.master, text="Regular Morning Rate", font="arial 25 bold")
        self.reg_mor_rate_e = Entry(self.master, width=20, font="arial 20 bold")

        self.reg_eve_quantity_l = Label(self.master, text="Regular Evening Quantity", font="arial 25 bold")
        self.reg_eve_quantity_e = Entry(self.master, width=20, font="arial 20 bold")

        self.reg_eve_rate_l = Label(self.master, text="Regular Evening Rate", font="arial 25 bold")
        self.reg_eve_rate_e = Entry(self.master, width=20, font="arial 20 bold")

        self.tBox = Text(self.master, width=50, height=20)

        self.id_l = Label(self.master, text="Enter Id", font="arial 25 bold")
        self.id_e = Entry(self.master, width=10, font="arial 20 bold")

        self.btn_add_to_db = Button(self.master, text="Add to Database", font="arial 10 bold", width=20, height=2, bg='lightgreen', fg='white', command=self.add_to_db)

        self.btn_retrive = Button(self.master, text="Retrive", font="arial 10 bold", width=10, height=2, bg='lightgreen', fg='white', command=self.retrive_info)

        self.btn_update = Button(self.master, text="Update ", font="arial 10 bold", width=15, height=2, bg='lightgreen', fg='white', command=self.update_to_db)
        
        self.btn_delete = Button(self.master, text="Delete ", font="arial 10 bold", width=15,height=2, bg="red", fg="white", command=self.delete_record)
        

    def place_fields(self, *args, **kwargs):
        # name
        self.name_l.place(x=20, y=210)      
        self.name_e.place(x=500, y=210)

        # address
        self.address_l.place(x=20, y=260)
        self.address_e.place(x=500, y=260)

        # phone        
        self.phone_l.place(x=20, y=310)
        self.phone_e.place(x=500, y=310)

        # regular morning quantity        
        self.reg_mor_quantity_l.place(x=20, y=360)
        self.reg_mor_quantity_e.place(x=500, y=360)

        # regular morning rate        
        self.reg_mor_rate_l.place(x=20, y=410)
        self.reg_mor_rate_e.place(x=500, y=410)

        #regular evening quantity        
        self.reg_eve_quantity_l.place(x=20, y=460)
        self.reg_eve_quantity_e.place(x=500, y=460)

        #regular evening rate        
        self.reg_eve_rate_l.place(x=20, y=510)
        self.reg_eve_rate_e.place(x=500, y=510)
    
    def empty_fields(self, *args, **kwargs):
        self.name_e.delete(0, END)
        self.address_e.delete(0, END)
        self.phone_e.delete(0, END)
        self.reg_mor_quantity_e.delete(0, END)
        self.reg_mor_rate_e.delete(0, END)
        self.reg_eve_quantity_e.delete(0, END)
        self.reg_eve_rate_e.delete(0, END)
        self.id_e.delete(0, END)
        self.tBox.delete('1.0', END)
        
        
    
    def forget_field(self, *args, **kwargs):
        self.name_l.place_forget()
        self.name_e.place_forget()
        self.address_l.place_forget()
        self.address_e.place_forget()
        self.phone_l.place_forget()
        self.phone_e.place_forget()
        self.reg_mor_quantity_l.place_forget()
        self.reg_mor_quantity_e.place_forget()
        self.reg_mor_rate_l.place_forget()
        self.reg_mor_rate_e.place_forget()
        self.reg_eve_quantity_l.place_forget()
        self.reg_eve_quantity_e.place_forget()
        self.reg_eve_rate_l.place_forget()
        self.reg_eve_rate_e.place_forget()
        self.id_l.place_forget()
        self.id_e.place_forget()
        self.btn_add_to_db.place_forget()
        self.btn_retrive.place_forget()
        self.btn_update.place_forget()
        self.btn_delete.place_forget()
        
        

    def get_field_entries(self, *args, **kwargs):
        self.name = self.name_e.get()
        self.address = self.address_e.get()
        self.phone = self.phone_e.get()
        self.reg_mor_quantity = self.reg_mor_quantity_e.get()
        self.reg_mor_rate = self.reg_mor_rate_e.get()
        self.reg_eve_quantity = self.reg_eve_quantity_e.get()
        self.reg_eve_rate = self.reg_eve_rate_e.get()


    
    def add_new_customer(self, *args, **kwargs):
        self.forget_field()
        self.empty_fields()
        self.place_fields()
        self.name_e.focus()

        # Text Box        
        self.tBox.place(x=900, y=210)

        # add to db button        
        self.btn_add_to_db.place(x=500, y=560)

    def add_to_db(self, *args, **kwargs):  # pylint: disable=E0202
        
        self.get_field_entries()

        if self.name == '' or self.address == '' or self.reg_mor_quantity == '' or self.reg_mor_rate == '' or self.reg_eve_quantity == '' or self.reg_eve_rate == '':
            tkinter.messagebox.showinfo("Error","Required Information Missing")
        else:
            query = "INSERT INTO customer (name,address,phone,regular_morning_quantity,regular_morning_rate,regular_evening_quantity,regular_evening_rate,pending_amount) VALUES (?,?,?,?,?,?,?,?)"
            self.c.execute(query, (self.name, self.address, self.phone, self.reg_mor_quantity, self.reg_mor_rate, self.reg_eve_quantity, self.reg_eve_rate, int(0)))
            self.conn.commit()
            
            self.empty_fields()
            self.forget_field()
            self.btn_add_to_db.place_forget()
            
            self.tBox.insert(END,"\n"+str(self.name)+" is successfully Added.")
            # tkinter.messagebox.showinfo("Success", "Successfully Added.")
            

    
    def update_existing(self, *args, **kwargs):

        self.forget_field()
        self.empty_fields()

        # id
        self.id_l.place(x=20, y=160)        
        self.id_e.place(x=500, y=160)
        self.id_e.focus()

        # Text Box
        self.tBox.place(x=900, y=210)

        # retrive btn
        self.btn_retrive.place(x=700, y=160)

        self.show_all_records()
    
    def show_all_records(self, *args, **kwargs):
        # query to show all id with name
        query = "SELECT id,name,address FROM customer"
        result = self.c.execute(query)
        result=result.fetchall()
        self.conn.commit()
        self.tBox.delete('1.0',END)
        self.tBox.insert(END, "\nid\tname\t\taddress\n")
        for r in result:
            self.tBox.insert(END, "\n"+str(r[0])+"\t"+str(r[1])+"\t\t"+str(r[2]))
    
    def retrive_info(self, *args, **kwargs):
        
        if self.id_e.get() == '':
            return

        self.place_fields()
        
        

        query = "SELECT * FROM customer WHERE id=?"
        results = self.c.execute(query, (self.id_e.get(),))
        
        # entry retrived information to respective field
        for result in results:
            self.id = result[0]
            self.name_e.delete(0, END)
            self.address_e.delete(0, END)
            self.phone_e.delete(0, END)
            self.reg_mor_quantity_e.delete(0, END)
            self.reg_mor_rate_e.delete(0, END)
            self.reg_eve_quantity_e.delete(0, END)
            self.reg_eve_rate_e.delete(0, END)
            self.name_e.insert(0, str(result[1]))
            self.address_e.insert(0, str(result[2]))
            self.phone_e.insert(0, str(result[3]))
            self.reg_mor_quantity_e.insert(0, str(result[4]))
            self.reg_mor_rate_e.insert(0, str(result[5]))
            self.reg_eve_quantity_e.insert(0, str(result[6]))
            self.reg_eve_rate_e.insert(0, str(result[7]))

        self.conn.commit()

        # place delete and update button
        self.btn_delete.place(x=500, y=560)
        self.btn_update.place(x=675, y=560)

    def update_to_db(self, *args, **kwargs):
        self.get_field_entries()

        if self.name == '' or self.address == '' or self.reg_mor_quantity == '' or self.reg_mor_rate == '' or self.reg_eve_quantity == '' or self.reg_eve_rate == '':
            tkinter.messagebox.showinfo("Error","Required Information Missing")
        else:
            query = "UPDATE customer SET name=?,address=?,phone=?,regular_morning_quantity=?,regular_morning_rate=?,regular_evening_quantity=?,regular_evening_rate=? WHERE id=?"
            self.c.execute(query, (self.name, self.address, self.phone, self.reg_mor_quantity, self.reg_mor_rate, self.reg_eve_quantity, self.reg_eve_rate, self.id))
            self.conn.commit()

            self.empty_fields()
            self.forget_field()
            
            self.id_e.delete(0, END)
            
            self.tBox.insert(END,"\n Id number "+str(self.id)+", "+str(self.name)+" is successfully Updated.")
            # tkinter.messagebox.showinfo("Success", "Successfully Updated.")

            self.id_e.focus()
        
    def delete_record(self, *args, **kwargs):
        self.get_field_entries()

        query = "DELETE  FROM customer WHERE id=?"
        self.c.execute(query, (self.id,))
        self.conn.commit()

        self.empty_fields()
        self.forget_field()
        self.id_e.delete(0, END)

        self.tBox.insert(END,"\n Id number "+str(self.id)+", "+str(self.name)+" is successfully Deleted.")




if __name__ == "__main__":
    
    root = Tk()
    b = Database(root)
    root.geometry("1366x768+0+0")
    root.title("Add customer")
    root.mainloop()
