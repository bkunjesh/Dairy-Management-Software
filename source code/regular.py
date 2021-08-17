from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3
import datetime
import os
import db
# http://www.science.smith.edu/dftwiki/index.php/File:TkInterColorCharts.png

# pyinstaller - https://pypi.org/project/pyinstaller/ 

days = [i for i in range(1, 32)]
months = [i for i in range(1, 13)]
years = [i for i in range(2020, 2030)]
shifts = ["Morning", "Evening"]

class GenerateBill:
    def __init__(self,*args,**kwargs):
        self.invoice=""
        self.make_bill_layout()
    
    def make_bill_layout(self, *args, **kwargs):
        heading = "\t\t\t\t\tJay Shree Krishna\t\t\t\t\t\n\n"
        self.invoice+=heading
    
    def add_next_line_to_bill(self, next_entry="", *args, **kwargs):
        self.invoice += next_entry + "\n"

    def print_invoice(self, *args, **kwargs):
        print(self.invoice)

    def generatebill_to_directory(self, directory="",file_name="", *args, **kwargs):
        if directory == "":
            return
        if not os.path.exists(directory):
            os.makedirs(directory)
        file = open(file_name, 'w')
        file.write(self.invoice)
        file.close()
        

# https://stackoverflow.com/questions/27820178/how-to-add-placeholder-to-an-entry-in-tkinter
# class EntryWithPlaceholder(tkinter.Entry):
#     def __init__(self, master=None,width=10,font="arial 115 bold", placeholder="PLACEHOLDER", color='grey'):
#         super().__init__(master)

#         self.placeholder = placeholder
#         self.placeholder_color = color
#         self.default_fg_color = self['fg']
#         self['font']=font
#         self['width']=width
        

#         self.bind("<FocusIn>", self.foc_in)
#         self.bind("<FocusOut>", self.foc_out)

#         self.put_placeholder()

#     def put_placeholder(self):
#         self.insert(0, self.placeholder)
#         self['fg'] = self.placeholder_color

#     def foc_in(self, *args):
#         if self['fg'] == self.placeholder_color:
#             self.delete('0', 'end')
#             self['fg'] = self.default_fg_color

#     def foc_out(self, *args):
#         if not self.get():
#             self.put_placeholder()

class Main:
    def __init__(self, master, *args, **kwargs):
        
        self.master = master

        
        # Frames
        self.color="ivory1"
        self.heading_frame = Frame(self.master, width=1366, height=50, bg="#B2F7EF")
        self.date_frame = Frame(self.master, width=1366, height=40, bg="#F7D6E0")
        self.features_frame = Frame(self.master, width=1366, height=40, bg="#6A6262")  #6A6262

        self.working_labelframe = LabelFrame(self.master, width=695, height=460, fg="green", font="arial 15 bold", text="Working Frame", bg=self.color)
        self.working_frame = Frame(self.working_labelframe, width=705, height=470, bg=self.color)  #5C6F68        
        
        self.display_frame = Frame(self.master, width=666, height=410, bg=self.color)   #AC8887
        self.customer_frame = Frame(self.master, width=666, height=180, bg=self.color)   #CF995F
        self.change_frame = Frame(self.working_frame, width=700, height=550, bg=self.color)   #5C6F68
        self.add_new_frame = Frame(self.working_frame, width=700, height=550, bg=self.color)   #5C6F68
        self.add_new_after_retrive_frame = Frame(self.working_frame, width=700, height=400, bg=self.color)#CF995F
        self.report_frame = Frame(self.working_frame, width=700, height=550, bg=self.color)   #5C6F68
        self.log_frame = Frame(self.master, width=700, height=130, bg=self.color)  #6A6262
        self.update_payment_frame = Frame(self.working_frame, width=700, height=470, bg=self.color)  #5C6F68

        self.display_labelframe = LabelFrame(self.display_frame, width=650, height=408, fg="green", font="arial 15 bold", text="Display Frame", bg=self.color)
        self.display_labelframe.place(x=4, y=0)

        self.customer_labelframe = LabelFrame(self.customer_frame, width=650, height=180, fg="green", font="arial 15 bold", text="Customers Data", bg=self.color)
        self.customer_labelframe.place(x=4, y=0)

        
        

        # place frames
        self.heading_frame.place(x=0, y=0)
        self.date_frame.place(x=0, y=55)
        self.features_frame.place(x=0, y=100)
        self.working_labelframe.place(x=0, y=145)
        self.working_frame.place(x=0, y=0)
        self.display_frame.place(x=710, y=145)
        self.customer_frame.place(x=710, y=570)
        self.log_frame.place(x=0, y=620)
        
        # heading
        self.heading = Label(self.heading_frame, text="Transactions", bg="#B2F7EF", font="arial 25 bold")
        self.heading.place(x=600, y=0)

        # make layout_frame
        self.make_date_frame()

        # Connection to database
        day = str(self.day_var.get())
        month = str(self.month_var.get())
        year = str(self.year_var.get())
        year = "2022"
        
        
        # path = "D:\project\kaalindi app\database\customers.db"
        # path = data_path + filename + '.db'
        self.conn = db.make_connection()
        self.c = self.conn.cursor()

        self.make_features_frame()
        self.make_display_frame()
        self.make_customer_frame()
        self.make_log_frame()

        

        
        # temporary
        
        



    

    def make_date_frame(self, *args, **kwargs):
        # label
        self.date_l = Label(self.date_frame, text="Date ", bg="#F7D6E0", font="arial 22 bold")
        self.date_l.place(x=10, y=0)
        # Option menu
        self.day_var = StringVar(self.date_frame)
        self.day_var.set(datetime.date.today().day)
        self.month_var = StringVar()
        self.month_var.set(datetime.date.today().month)
        self.year_var = StringVar()
        self.year_var.set(datetime.date.today().year)

        self.day_optionmenu = OptionMenu(self.date_frame, self.day_var, *days)
        self.day_optionmenu.place(x=90, y=6)
        self.month_optionmenu = OptionMenu(self.date_frame, self.month_var, *months)
        self.month_optionmenu.place(x=150, y=6)
        self.year_optionmenu = OptionMenu(self.date_frame, self.year_var, *years)
        self.year_optionmenu.place(x=210, y=6)

        self.day_var.trace('w', self.get_date)
        self.month_var.trace('w', self.get_date)
        self.year_var.trace('w', self.get_date)

    def get_date(self, *args):
        self.curr_day = str(self.day_var.get())
        self.curr_month = str(self.month_var.get())
        self.curr_year = str(self.year_var.get())
        # print(self.curr_day + "-" + self.curr_month + "-" + self.curr_year)
        return [self.curr_day, self.curr_month, self.curr_year]

    def make_features_frame(self, *args, **kwargs):
        
        # butoon for home
        self.btn_update_payment = Button(self.features_frame, text="Home", font="arial 9 bold", width=15, height=2,command=self.btn_home_pressed)
        self.btn_update_payment.place(x=10, y=0)
        # add all expected tansaction to database button
        self.btn_add_all_expected = Button(self.features_frame, text="Add All Expected tansaction",font="arial 9 bold", width=25, height=2,command=self.btn_add_all_expected_pressed)
        self.btn_add_all_expected.place(x=130, y=0)
        
        # add new tansaction button
        self.btn_add_new = Button(self.features_frame, text="Add new transaction",font="arial 9 bold", width=25, height=2,command=self.btn_add_new_pressed)
        self.btn_add_new.place(x=320, y=0)

        # show transaction button
        self.btn_report = Button(self.features_frame, text="Transaction Report", font="arial 9 bold", width=25, height=2,command=self.btn_report_pressed)
        self.btn_report.place(x=510, y=0)

        # payment updation Button
        self.btn_update_payment = Button(self.features_frame, text="Update Payment", font="arial 9 bold", width=25, height=2,command=self.btn_update_payment_pressed)
        self.btn_update_payment.place(x=700, y=0)
        
        

    def make_display_frame(self, *args, **kwargs):
        # Listbox for display
        self.display_listbox = Listbox(self.display_frame, width=100, height=25)
        # self.display_listbox.place(x=28, y=28)

        # TreeView for display
        self.display_treeview = ttk.Treeview(self.display_frame, height=15)
            
        
        # Constructing vertical scrollbar with treeview 
        # display_verscrlbar = ttk.Scrollbar(self.display_frame,orient ="vertical",command = self.display_treeview.yview)        
        # # Calling pack method w.r.to verical scrollbar 
        # display_verscrlbar.pack(side='right', fill='x')        
        # # Configuring treeview 
        # self.display_treeview.configure(xscrollcommand=display_verscrlbar.set)
        
        # formate our display treeview

        self.display_treeview['column'] = ("Transaction_id", "Customer_id", "Customer_name", "Date", "Quantity", "Price", "Shift")
        self.display_treeview['show'] = 'headings'
        
        self.display_treeview.column("Transaction_id",anchor=W,width=90)
        self.display_treeview.column("Customer_id",anchor=W,width=80)
        self.display_treeview.column("Customer_name",anchor=W,width=140)
        self.display_treeview.column("Date",anchor=W,width=80)
        self.display_treeview.column("Quantity",anchor=W,width=70)
        self.display_treeview.column("Price",anchor=W,width=80)
        self.display_treeview.column("Shift", anchor=W, width=80)

        self.display_treeview.heading("Transaction_id",text="Transaction_id",anchor=W)
        self.display_treeview.heading("Customer_id",text="Customer_id",anchor=W)
        self.display_treeview.heading("Customer_name", text="Customer_name", anchor=W)
        self.display_treeview.heading("Date", text="Date", anchor=W)
        self.display_treeview.heading("Quantity", text="Quantity", anchor=W)
        self.display_treeview.heading("Price", text="Price", anchor=W)
        self.display_treeview.heading("Shift", text="Shift", anchor=W)
        
        self.display_treeview.place(x=10, y=28)



        vsb_display_treeview = ttk.Scrollbar(self.display_frame, orient="vertical", command=self.display_treeview.yview)
        # vsb.place(x=630,y=28)
        vsb_display_treeview.place(relx=0.9490, rely=0.07, relheight=0.790, relwidth=0.020)
        self.display_treeview.configure(yscrollcommand=vsb_display_treeview.set)

        # Change
        self.btn_change = Button(self.display_frame, text="Change",font="arial 10 bold", width=10, height=2,bg="lightGreen",command=self.btn_change_pressed)
        self.btn_change.place(x=540, y=359)
        # delete
        self.btn_delete = Button(self.display_frame, text="Clear",font="arial 10 bold", width=10, height=2,bg="indian red",command=self.btn_clear_pressed)
        self.btn_delete.place(x=430, y=359)

    def make_log_frame(self, *args, **kwargs):
        self.inlog_tbox = Text(self.log_frame, width=80, height=6)
        self.inlog_tbox.place(x=20, y=14)
        vsb_tbox = ttk.Scrollbar(self.log_frame, orient="vertical", command=self.inlog_tbox.yview)
        # vsb.place(x=630,y=28)
        vsb_tbox.place(relx=0.9490, rely=0.099, relheight=0.780, relwidth=0.020)
        self.inlog_tbox.configure(yscrollcommand=vsb_tbox.set)


        
    def make_customer_frame(self, *args, **kwargs):
        # text box
        # self.tbox = Text(self.log_frame, width=75, height=5)
        # self.tbox.place(x=28, y=14)

        # TreeView for customer detail
        self.customer_treeview = ttk.Treeview(self.customer_frame, height=6)

        # formate customer detail view
        self.customer_treeview['column'] = ("Customer_id", "Customer_name", "Address")
        self.customer_treeview['show'] = 'headings'

        self.customer_treeview.column("Customer_id", anchor=W, width=80)
        self.customer_treeview.column("Customer_name", anchor=W, width=240)
        self.customer_treeview.column("Address", anchor=W, width=240)

        self.customer_treeview.heading("Customer_id",text="Customer_id",anchor=W)
        self.customer_treeview.heading("Customer_name", text="Customer_name", anchor=W)
        self.customer_treeview.heading("Address", text="Address", anchor=W)

        self.customer_treeview.place(x=45, y=27)

        vsb_customer_treeview = ttk.Scrollbar(self.customer_frame, orient="vertical", command=self.customer_treeview.yview)
        # vsb.place(x=630,y=28)
        vsb_customer_treeview.place(relx=0.912, rely=0.15, relheight=0.819, relwidth=0.020)
        
        self.customer_treeview.configure(yscrollcommand=vsb_customer_treeview.set)
        
        # enter detail of all customer in customer tree
        customers_query = "SELECT * FROM customer"
        all_customer = self.c.execute(customers_query)
        all_customer = self.c.fetchall()
        for customer in all_customer:
            Treeview_entry = (customer[0], customer[1], customer[2])
            self.customer_treeview.insert('', 'end', text='', values=Treeview_entry)

    def make_change_frame(self, *args, **kwargs):

        self.change_frame.destroy()
        self.change_frame = Frame(self.working_frame, width=700, height=550,bg=self.color)

        # Transaction Id label and entry in change frame
        self.inchange_tran_id_l = Label(self.change_frame, text="transaction id", font="arial 18 bold",bg=self.color)
        self.inchange_tran_id_l.place(x=10, y=10)

        self.inchange_tran_id_e = Entry(self.change_frame, width=10, font="arial 18 bold")
        self.inchange_tran_id_e.place(x=180, y=10)
        

        # Date label in change frame
        self.inchange_date_l = Label(self.change_frame, text="date (dd/mm/yy) ", font="arial 18 bold",bg=self.color)
        self.inchange_date_l.place(x=10, y=70)

        # date entry in change frame
        self.inchange_day_e = Entry(self.change_frame, width=3, font="arial 18 bold")
        self.inchange_day_e.place(x=230,y=70)
        self.inchange_month_e = Entry(self.change_frame, width=3, font="arial 18 bold")
        self.inchange_month_e.place(x=280,y=70)
        self.inchange_year_e = Entry(self.change_frame, width=5, font="arial 18 bold")
        self.inchange_year_e.place(x=330,y=70)

        # customer id label and entry in change frame

        self.inchange_customer_id_l = Label(self.change_frame, text="customer id", font="arial 18 bold",bg=self.color)
        self.inchange_customer_id_l.place(x=10, y=130)

        self.inchange_customer_id_e = Entry(self.change_frame, width=10, font="arial 18 bold")
        self.inchange_customer_id_e.place(x=180, y=130)

        #shift menue in change frame
        self.inchange_shift = StringVar(self.change_frame)
        # self.inchange_shift.set(shifts[0])
        self.inchange_shifts_optionmenue = OptionMenu(self.change_frame, self.inchange_shift, *shifts)
        self.inchange_shifts_optionmenue.place(x=360,y=130)

        # retrive button in change frame
        # self.btn_inchange_retrive = Button(self.change_frame, text="Retrive", font="arial 15 bold", bg="red")
        # self.btn_inchange_retrive.place(x=590,y=130)

        # name label and entry in change frame
        self.inchange_name_l = Label(self.change_frame, text="Name", font="arial 18 bold",bg=self.color)
        self.inchange_name_l.place(x=10, y=210)

        self.inchange_name_e = Entry(self.change_frame, width=30, font="arial 18 bold")
        self.inchange_name_e.place(x=90,y=210)

        # address label in change frame
        # self.inchange_address_l = Label(self.change_frame, text="Address", font="arial 18 bold")
        # self.inchange_address_l.place(x=10, y=270)       

        # morning lable in change frame
        # self.inchange_shift_l = Label(self.change_frame, text="Shift", font="arial 18 bold")
        # self.inchange_shift_l.place(x=10, y=340)

        
        # price Entry in change frame
        self.inchange_rate_e = Entry(self.change_frame, width=10, font="arial 18 bold")
        self.inchange_rate_e.place(x=120, y=280)

        self.inchange_rate_l = Label(self.change_frame, text="Rs.", font="arial 18 bold",bg=self.color)
        self.inchange_rate_l.place(x=260,y=280)

        # quantity entry in change frame
        self.inchange_quantity_e = Entry(self.change_frame, width=10, font="arial 18 bold")
        self.inchange_quantity_e.place(x=350, y=280)

        self.inchange_quantity_l = Label(self.change_frame, text="Liter", font="arial 18 bold",bg=self.color)
        self.inchange_quantity_l.place(x=490,y=280)
        
        # update changes button in change frame
        self.btn_inchange_update = Button(self.change_frame, text="Update Changes", font="arial 15 bold", bg="lightgreen",command=self.btn_inchange_update_pressed)
        self.btn_inchange_update.place(x=500, y=350)

        
        
    def make_add_new_frame(self, *args, **kwargs):
        # customer id for retrive his/her other information
        self.inaddnew_id_l = Label(self.add_new_frame, text="Customer id", font="arial 18 bold",bg=self.color)
        self.inaddnew_id_l.place(x=10, y=10)

        self.inaddnew_id_e = Entry(self.add_new_frame, width=10, font="arial 20 bold")
        self.inaddnew_id_e.place(x=200, y=10)
        
        # retrive button
        self.btn_inaddnew_retrive = Button(self.add_new_frame, text="Retrive", font="arial 15 bold",bg="lightgreen",command=self.inaddnew_btn_retrive_pressed)
        self.btn_inaddnew_retrive.place(x=400, y=10)

    def make_update_payment_frame(self,*args,**kwargs):
        self.inupdatepayment_id_l = Label(self.update_payment_frame, text="Customer id", font="arial 18 bold",bg=self.color)
        self.inupdatepayment_id_l.place(x=10, y=10)

        self.inupdatepayment_id_e=Entry(self.update_payment_frame, width=10, font="arial 20 bold")
        self.inupdatepayment_id_e.place(x=200, y=10)
        
        self.inupdatepayment_payment_date_l = Label(self.update_payment_frame, text="Payment Date(dd-mm-yyyy)", font="arial 18 bold",bg=self.color)
        self.inupdatepayment_payment_date_l.place(x=10, y=60)


        day = self.get_date()[0]
        month = self.get_date()[1]
        year = self.get_date()[2]
        self.inupdatepayment_Payment_day_e=Entry(self.update_payment_frame, width=3, font="arial 20 bold")
        self.inupdatepayment_Payment_month_e=Entry(self.update_payment_frame, width=3, font="arial 20 bold")
        self.inupdatepayment_Payment_year_e=Entry(self.update_payment_frame, width=5, font="arial 20 bold")
        self.inupdatepayment_Payment_day_e.place(x=350, y=60)
        self.inupdatepayment_Payment_day_e.insert(0,day)
        self.inupdatepayment_Payment_month_e.place(x=410, y=60)
        self.inupdatepayment_Payment_month_e.insert(0,month)
        self.inupdatepayment_Payment_year_e.place(x=470, y=60)
        self.inupdatepayment_Payment_year_e.insert(0,year)

        self.inupdatepayment_amount_l = Label(self.update_payment_frame, text="Payment Amount", font="arial 18 bold",bg=self.color)
        self.inupdatepayment_amount_l.place(x=10, y=110)

        self.inupdatepayment_amount_e=Entry(self.update_payment_frame, width=7, font="arial 20 bold")
        self.inupdatepayment_amount_e.place(x=220, y=110)
        self.inupdatepayment_amountrs_l = Label(self.update_payment_frame, text="Rs.", font="arial 18 bold",bg=self.color)
        self.inupdatepayment_amountrs_l.place(x=340, y=110)

        self.btn_inupdatepayment_add_payment = Button(self.update_payment_frame, text="Add Payment", font="arial 15 bold",bg="lightgreen",command=self.inupdatepayment_add_payment_pressed)
        self.btn_inupdatepayment_add_payment.place(x=500, y=160)
    
    def make_report_frame(self, *args, **kwargs):

        # customer id in report frame
        self.inreport_id_l=Label(self.report_frame, text="Customer id", font="arial 18 bold",bg=self.color)
        self.inreport_id_l.place(x=10, y=10)

        self.inreport_id_e = Entry(self.report_frame, width=10, font="arial 20 bold")
        self.inreport_id_e.delete(0,END)
        self.inreport_id_e.place(x=200, y=10)

        # day in report frame
        self.inreport_day_l=Label(self.report_frame, text="Day", font="arial 18 bold",bg=self.color)
        self.inreport_day_l.place(x=10, y=60)

        self.inreport_day_e = Entry(self.report_frame, width=3, font="arial 20 bold")
        self.inreport_day_e.delete(0, END)
        self.inreport_day_e.place(x=65, y=60)

        # month in report frame
        self.inreport_month_l = Label(self.report_frame, text="Month", font="arial 18 bold",bg=self.color)
        self.inreport_month_l.place(x=120, y=60)

        self.inreport_month_e = Entry(self.report_frame, width=3, font="arial 20 bold")
        self.inreport_month_e.delete(0, END)
        self.inreport_month_e.place(x=205, y=60)

        # year in report frame
        self.inreport_year_l = Label(self.report_frame, text="Year", font="arial 18 bold",bg=self.color)
        self.inreport_year_l.place(x=260, y=60)

        self.inreport_year_e = Entry(self.report_frame, width=5, font="arial 20 bold")
        self.inreport_year_e.delete(0, END)
        self.inreport_year_e.place(x=320, y=60)

        # fetch Button in report frame
        self.btn_inreport_fetch = Button(self.report_frame, text="Fetch",width=10, font="arial 15 bold",bg="lightgreen",command=self.btn_inreport_fetch_pressed)
        self.btn_inreport_fetch.place(x=500, y=110)
    
    def btn_clear_pressed(self, *args, **kwargs):
        for entry in self.display_treeview.get_children():
            self.display_treeview.delete(entry)

        

    def inaddnew_btn_retrive_pressed(self, *args, **kwargs):
        self.add_new_after_retrive_frame.place_forget()

        self.inaddnew_name_l=None
        self.make_layout_after_retrive_pressed()
    
    

    def make_layout_after_retrive_pressed(self, *args, **kwargs):
        customer_id = (self.inaddnew_id_e.get())
        if customer_id == '':
            tkinter.messagebox.showinfo("Error", "Required Information Missing")
        else:
            select_query = "SELECT * FROM customer WHERE id=?"
            result = self.c.execute(select_query, (customer_id,))
            result = result.fetchone()
            self.conn.commit()
            if result==None:
                tkinter.messagebox.showinfo("Error", "Enter valid customer id :(")
            else:
                # destroy frame and initialize again
                self.add_new_after_retrive_frame.destroy()
                self.add_new_after_retrive_frame=Frame(self.working_frame,width=700,height=400,bg=self.color)

                # name label in add new frame

                self.inaddnew_name_l = Label(self.add_new_after_retrive_frame, text=result[1], font="arial 18 bold",bg=self.color)
                self.inaddnew_name_l.place(x=10, y=50)

                # address label in add new frame
                self.inaddnew_address_l = Label(self.add_new_after_retrive_frame, text=result[2], font="arial 18 bold",bg=self.color)
                self.inaddnew_address_l.place(x=380, y=50)

                # date lable in add new frame
                self.inaddnew_date_l = Label(self.add_new_after_retrive_frame, text="Date(dd/mm/yy)", font="arial 18 bold",bg=self.color)
                self.inaddnew_date_l.place(x=10, y=100)
                
                self.inaddnew_day_e = Entry(self.add_new_after_retrive_frame, width=3, font="arial 18 bold")
                self.inaddnew_day_e.place(x=210, y=100)
                self.inaddnew_month_e = Entry(self.add_new_after_retrive_frame, width=3, font="arial 18 bold")
                self.inaddnew_month_e.place(x=270, y=100)
                self.inaddnew_year_e = Entry(self.add_new_after_retrive_frame, width=5, font="arial 18 bold")
                self.inaddnew_year_e.place(x=330, y=100)
                
                day = self.get_date()[0]
                month = self.get_date()[1]
                year = self.get_date()[2]

                self.inaddnew_day_e.delete(0,END)
                self.inaddnew_month_e.delete(0,END)
                self.inaddnew_year_e.delete(0,END)
                self.inaddnew_day_e.insert(0,day)
                self.inaddnew_month_e.insert(0,month)
                self.inaddnew_year_e.insert(0,year)


                # morning lable in add new frame
                self.inaddnew_mor_l = Label(self.add_new_after_retrive_frame, text="Morning", font="arial 18 bold",bg=self.color)
                self.inaddnew_mor_l.place(x=10, y=150)

                # price Entry in add new frame
                self.inaddnew_mor_rate_e = Entry(self.add_new_after_retrive_frame, width=10, font="arial 18 bold")
                self.inaddnew_mor_rate_e.place(x=150, y=150)
                self.inaddnew_mor_rate_e.delete(0,END)  
                self.inaddnew_mor_rate_e.insert(0,result[5])

                # quantity entry in add new frame
                self.inaddnew_mor_lit_e = Entry(self.add_new_after_retrive_frame, width=10, font="arial 18 bold")
                self.inaddnew_mor_lit_e.place(x=350, y=150)
                self.inaddnew_mor_lit_e.delete(0, END)
                self.inaddnew_mor_lit_e.insert(0,result[4])

                # eveing lable in add new frame
                self.inaddnew_eve_l = Label(self.add_new_after_retrive_frame, text="Evening", font="arial 18 bold",bg=self.color)
                self.inaddnew_eve_l.place(x=10, y=200)

                # price Entry in add new frame
                self.inaddnew_eve_rate_e = Entry(self.add_new_after_retrive_frame, width=10, font="arial 18 bold")
                self.inaddnew_eve_rate_e.place(x=150, y=200)
                self.inaddnew_eve_rate_e.delete(0, END)
                self.inaddnew_eve_rate_e.insert(0,result[7])

                # quantity entry in add new frame
                self.inaddnew_eve_lit_e = Entry(self.add_new_after_retrive_frame, width=10, font="arial 18 bold")
                self.inaddnew_eve_lit_e.place(x=350, y=200)
                self.inaddnew_eve_lit_e.delete(0, END)
                self.inaddnew_eve_lit_e.insert(0,result[6])
                
                # update changes button in add new frame
                self.btn_inaddnew_addnewtransaction = Button(self.add_new_after_retrive_frame, text="Add New Transaction", font="arial 15 bold", bg="lightgreen", command=self.btn_inaddnew_addnewtransaction_pressed)
                self.btn_inaddnew_addnewtransaction.place(x=470, y=270)
                
                self.add_new_after_retrive_frame.place(x=0, y=100)

    def empty_inchange_entries(self, *args, **kwargs):
        self.inchange_tran_id_e.delete(0, END)
        self.inchange_day_e.delete(0, END)
        self.inchange_month_e.delete(0, END)
        self.inchange_year_e.delete(0, END)
        self.inchange_customer_id_e.delete(0, END)
        self.inchange_name_e.delete(0, END)
        self.inchange_quantity_e.delete(0, END)
        self.inchange_rate_e.delete(0, END)

    def btn_inaddnew_addnewtransaction_pressed(self, *args, **kwargs):
        customer_id = self.inaddnew_id_e.get()
        day = (self.inaddnew_day_e.get())
        month = self.inaddnew_month_e.get()
        year = self.inaddnew_year_e.get()
        if int(day) > 9:
            date = str(day) + "-" + str(month) + "-" + str(year)
        else:
            day = "0" + str(day)
            date = str(day) + "-" + str(month) + "-" + str(year)
        mor_rate = self.inaddnew_mor_rate_e.get()
        mor_quantity = self.inaddnew_mor_lit_e.get()
        mor_price=float(mor_rate)*float(mor_quantity)
        eve_rate = self.inaddnew_eve_rate_e.get()
        eve_quantity = self.inaddnew_eve_lit_e.get()
        eve_price=float(eve_rate)*float(eve_quantity)

        select_query = "SELECT * FROM customer WHERE id=?"
        result = self.c.execute(select_query, (customer_id,))
        result = result.fetchone()
        self.conn.commit()
        name = result[1]

        transaction_id_query = "SELECT MAX(transaction_id)  FROM item_transaction" 
        cur_transaction_id = self.c.execute(transaction_id_query)
        cur_transaction_id = cur_transaction_id.fetchone()[0]

        

        if float(mor_quantity) > 0 and float(mor_price) > 0:

            pending_amount = float(result[8])+mor_price
            update_query = "UPDATE customer set pending_amount=? where id=? "
            self.c.execute(update_query, (pending_amount, customer_id,))
            self.conn.commit()

            cur_transaction_id += 1
            transaction_query = "INSERT INTO item_transaction (customer_id,day,month,year,quantity,price,shift) VALUES (?,?,?,?,?,?,?)"
            
            self.c.execute(transaction_query, (customer_id,day,month,year,mor_quantity, mor_price, "Morning"))
            Treeview_entry = (cur_transaction_id, customer_id, name, date, mor_quantity, mor_price, "Morning")
            self.display_treeview.insert('', 'end', text='', values=Treeview_entry)
            

        if float(eve_quantity) > 0 and float(eve_price) > 0:
            
            pending_amount += eve_price
            update_query = "UPDATE customer set pending_amount=? where id=? "
            self.c.execute(update_query, (pending_amount, customer_id,))
            self.conn.commit()

            cur_transaction_id += 1
            transaction_query = "INSERT INTO item_transaction (customer_id,day,month,year,quantity,price,shift) VALUES (?,?,?,?,?,?,?)"
            
            self.c.execute(transaction_query, (customer_id,day,month,year,eve_quantity, eve_price, "Evening"))
            Treeview_entry = (cur_transaction_id, customer_id, name, date, eve_quantity, eve_price, "Evening")
            self.display_treeview.insert('', 'end', text='', values=Treeview_entry)

        # log massege
        Message_for_log = "New transaction for customer id "+str(customer_id)+" succseed :)"
        self.inlog_tbox.insert(END, ">\n"+Message_for_log+"\n")
            
            
        self.btn_add_new_pressed()
        self.conn.commit()
        
    def inupdatepayment_add_payment_pressed(self, *args, **kwargs):
        customer_id = self.inupdatepayment_id_e.get()
        date = str(self.inupdatepayment_Payment_day_e.get()) + "-" + str(self.inupdatepayment_Payment_month_e.get()) + "-" + str(self.inupdatepayment_Payment_year_e.get())
        amount = self.inupdatepayment_amount_e.get()

        if str(customer_id) == '' or str(self.inupdatepayment_Payment_day_e.get()) == '' or int(self.inupdatepayment_Payment_day_e.get()) < 0 or int(self.inupdatepayment_Payment_day_e.get()) >31 or str(self.inupdatepayment_Payment_month_e.get()) == '' or int(self.inupdatepayment_Payment_month_e.get()) < 0 or int(self.inupdatepayment_Payment_month_e.get()) > 12 or str(self.inupdatepayment_Payment_year_e.get()) == '' or int(self.inupdatepayment_Payment_year_e.get()) < 0 or str(self.inupdatepayment_amount_e.get()) == '' or int(self.inupdatepayment_amount_e.get()) == 0:
            tkinter.messagebox.showinfo("Error", "insufficent or null value!!! :(")
        else:
            
            # get current pending amount
            cur_pending_amt_query = "SELECT * FROM customer WHERE id=?"
            self.c.execute(cur_pending_amt_query, (int(customer_id),))
            customer = self.c.fetchone()
            if customer == None:
                tkinter.messagebox.showinfo("Error", "id doesn't exists!\nplease, check the customer id.")
            else:
                
                add_payment_query = "INSERT INTO payment (customer_id,payment_date,payment_amount) VALUES (?,?,?)"
                self.c.execute(add_payment_query, (int(customer_id), str(date), int(amount)))
                self.conn.commit()

                cur_pending = int(customer[8])

                update_payment_query = "UPDATE customer set pending_amount=? where id=?"
                pending = cur_pending - int(amount)
                # credit=max(customer[9]-amount,0)
                # if pending < 0:
                #     credit = abs(pending)
                #     pending=0
                # print(pending);
                self.c.execute(update_payment_query, (pending, customer_id))

                self.conn.commit()

                tkinter.messagebox.showinfo("Succses", str(amount) + " rs. has been updated for customer " + str(customer_id) + " ( " + str(customer[1]) + " )")

                self.inupdatepayment_id_e.delete(0,last='end')
                self.inupdatepayment_amount_e.delete(0, 'end')
                self.inupdatepayment_Payment_day_e.delete(0, 'end')
                self.inupdatepayment_Payment_month_e.delete(0, 'end')
                self.inupdatepayment_Payment_year_e.delete(0, 'end')
                day = self.get_date()[0]
                month = self.get_date()[1]
                year = self.get_date()[2]
                self.inupdatepayment_Payment_day_e.insert(0,day)
                self.inupdatepayment_Payment_month_e.insert(0,month)
                self.inupdatepayment_Payment_year_e.insert(0,year)
            




    def btn_update_payment_pressed(self, *args, **kwargs):
        
        self.change_frame.place_forget()
        self.add_new_frame.place_forget()
        self.add_new_after_retrive_frame.place_forget()
        self.report_frame.place_forget()
        self.update_payment_frame.place_forget()

        self.make_update_payment_frame()
        self.update_payment_frame.place(x=0,y=0)
        
    def btn_change_pressed(self, *args, **kwargs):

        self.change_frame.place_forget()
        self.add_new_frame.place_forget()
        self.add_new_after_retrive_frame.place_forget()
        self.report_frame.place_forget()
        self.update_payment_frame.place_forget()

        self.make_change_frame()
        self.change_frame.place(x=0, y=0)

        self.empty_inchange_entries()

        if len(self.display_treeview.selection())>0:
            curr_transaction = self.display_treeview.focus()
            curr_transaction = self.display_treeview.item(curr_transaction)['values']
            # print(curr_transaction[0])            

            self.inchange_tran_id_e.insert(0, curr_transaction[0])
            self.inchange_customer_id_e.insert(0, curr_transaction[1])
            self.inchange_name_e.insert(0, curr_transaction[2])
            self.inchange_quantity_e.insert(0, curr_transaction[4])
            curr_transaction_rate = float(curr_transaction[5])/float(curr_transaction[4])
            self.inchange_rate_e.insert(0, curr_transaction_rate)

            if curr_transaction[3][1]!='-':
                day = str(curr_transaction[3][0]) + str(curr_transaction[3][1])
                if curr_transaction[3][4]!='-':
                    month=str(curr_transaction[3][3])+str(curr_transaction[3][4])
                    year = str(curr_transaction[3][6]) + str(curr_transaction[3][7]) + str(curr_transaction[3][8]) + str(curr_transaction[3][9])
                else:
                    month=str(curr_transaction[3][3])
                    year = str(curr_transaction[3][5]) + str(curr_transaction[3][6]) + str(curr_transaction[3][7]) + str(curr_transaction[3][8])
            else:
                day = str(curr_transaction[3][0])
                if curr_transaction[3][3]!='-':
                    month=str(curr_transaction[3][2])+str(curr_transaction[3][3])
                    year = str(curr_transaction[3][5]) + str(curr_transaction[3][6]) + str(curr_transaction[3][7]) + str(curr_transaction[3][8])
                else:
                    month=str(curr_transaction[3][2])
                    year = str(curr_transaction[3][4]) + str(curr_transaction[3][5]) + str(curr_transaction[3][6]) + str(curr_transaction[3][7])

            self.inchange_day_e.insert(0, day)
            self.inchange_month_e.insert(0, month)
            self.inchange_year_e.insert(0, year)
            self.inchange_shift.set(curr_transaction[6])
        
    def btn_report_pressed(self, *args, **kwargs):
        self.change_frame.place_forget()
        self.add_new_frame.place_forget()
        self.add_new_after_retrive_frame.place_forget()
        self.report_frame.place_forget()
        self.update_payment_frame.place_forget()

        self.make_report_frame()   #empty entries code also wriiten in make_report_frame() function
        self.report_frame.place(x=0, y=0)
        
    def btn_inreport_fetch_pressed(self, *args, **kwargs):
        customer_id = (self.inreport_id_e.get())
        day = (self.inreport_day_e.get())
        month = (self.inreport_month_e.get())
        year = (self.inreport_year_e.get())
        if month == '' or year == '' or (day!='' and (int(day)>31 or int(day)<1)) or (int(month)>12 or int(month)<1) or len(str(year))!=4:
            tkinter.messagebox.showinfo("Error", "invalid request :(")
        else :
            # all posiible report
            self.btn_clear_pressed()
            self.fetch_transaction_call()
        
    def fetch_transaction_call(self, *args, **kwargs):

        customer_id = (self.inreport_id_e.get())
        day = (self.inreport_day_e.get())
        month = (self.inreport_month_e.get())
        year = (self.inreport_year_e.get())

        if customer_id == '':
            if str(day)!='':
                # daily transaction of all customer
                transaction_query = "SELECT * From item_transaction WHERE day =? AND month =? AND year =?"
                transactions = self.c.execute(transaction_query, (int(day), int(month), int(year)))
            else:
                # monthly transaction of all customer
                transaction_query = "SELECT * From item_transaction WHERE month =? AND year =?"
                transactions = self.c.execute(transaction_query, (int(month), int(year)))
        else:
            if str(day) != '':
                # daily transaction of one customer
                transaction_query = "SELECT * From item_transaction WHERE customer_id=? AND day =? AND month =? AND year =?"
                transactions = self.c.execute(transaction_query, (int(customer_id),int(day), int(month), int(year)))
            else:
                #  monthly transaction of one customer
                transaction_query = "SELECT * From item_transaction WHERE customer_id=? AND month =? AND year =?"
                transactions = self.c.execute(transaction_query, (int(customer_id), int(month), int(year)))

        total_liter = 0
        total_cost = 0
        
        transactions = self.c.fetchall()
        for transaction in transactions:
            customers_query = "SELECT * FROM customer WHERE id=?"
            customer = self.c.execute(customers_query, (transaction[1],))
            customer = self.c.fetchone()

            day = int(transaction[2])
            month = int(transaction[3])
            year = int(transaction[4])
            if int(day) > 9:
                date = str(day) + "-" + str(month) + "-" + str(year)
            else:
                day = "0" + str(day)
                date = str(day) + "-" + str(month) + "-" + str(year)

            # print(transaction)
            Treeview_entry = (transaction[0], transaction[1], customer[1], date, transaction[5], transaction[6], transaction[7])
            self.display_treeview.insert('', 'end', text='', values=Treeview_entry)
            total_liter += transaction[5]
            total_cost += transaction[6]
        self.conn.commit()

        # print status in log frame
        Message_for_log = "Total Liter : " + str(total_liter) + "\nTotal Cost: " + str(total_cost)
        if customer_id != '':
            Message_for_log = "For Customer id: "+str(customer_id)+"\n"+Message_for_log
        self.inlog_tbox.insert(END, ">\n" + Message_for_log + "\n")
        self.btn_inreport_print = Button(self.report_frame, text="Print", font="arial 15 bold", width=10, bg="red", command=lambda:self.btn_inreport_print_pressed(transactions,str(self.inreport_id_e.get()),str(self.inreport_day_e.get()),str(self.inreport_month_e.get()),str(self.inreport_year_e.get())))
        self.btn_inreport_print.place(x=500, y=160)
        
    def btn_inreport_print_pressed(self,transactions, customer_id, day, month, year,*args, **kwargs):
        # print("print press ho gaya :)")
        # print(len(customer_id))
        # print(len(day))
        # print(month)
        # print(year)
        # print(transactions)
        generateBill = GenerateBill()
        if month == '' or year == '':
            tkinter.messagebox.showinfo("Error", "invalid request :(")
        elif str(customer_id) != '' :  # 1)month report of a customer   2)daily report of customer

            customer_detail_query = "SELECT * FROM customer WHERE id=?"
            customer_detail = self.c.execute(customer_detail_query, (int(customer_id),))
            customer_detail = self.c.fetchone()

            next_line = "\tcustomer:" + str(customer_id) + "\t" + str(customer_detail[1]) + "\t" + str(customer_detail[2]) + "\n\n"
            next_line += "\t---------------------------------------------------------\n\tSn_no   Date(Shift)     Amount   Cost\n\t---------------------------------------------------------\n"
            generateBill.add_next_line_to_bill(next_line)
            sn_no = 1
            morning_quantity_sum = 0
            morning_cost_sum = 0
            evening_quantity_sum = 0
            evening_cost_sum=0
            for transaction in transactions:
                # print(transaction)
                date = str(transaction[2]) + "/" + str(transaction[3]) + "/" + str(transaction[4])
                shift = transaction[7][0]
                entry = "\t\t" + str(sn_no)+" "*int(2-len(str(sn_no))) + "       " + str(date)+" "*int(10-len(str(date)))+ " (" + str(shift) + ")   " + str(transaction[5]) + " lit.   " + str(transaction[6]) + " Rs."
                sn_no += 1
                generateBill.add_next_line_to_bill(entry)
                if shift == "M":
                    morning_quantity_sum += float(transaction[5])
                    morning_cost_sum += float(transaction[6])
                else:
                    evening_quantity_sum += float(transaction[5])
                    evening_cost_sum += float(transaction[6])
            
            total_liter = morning_quantity_sum + evening_quantity_sum
            total_cost=morning_cost_sum+evening_cost_sum

            end_line = "\n\n\n\t---------------------------------------------------------\n\tMorning Total liter: " + str(morning_quantity_sum) + " \tMorning Total Cost: " + str(morning_cost_sum) + "\n"
            end_line += "\t---------------------------------------------------------\n\tEvening Total liter: " + str(evening_quantity_sum) + " \tEvening Total Cost: " + str(evening_cost_sum) + "\n"
            end_line += "\t---------------------------------------------------------\n\t       Total liter: " + str(total_liter) + "         Total Cost: " + str(total_cost) + "\n"

            generateBill.add_next_line_to_bill(end_line)
            
                
            if day == '':
                # month report of a customer
                prev_due=float(customer_detail[8])-float(total_cost)
                total_due=float(customer_detail[8])
                bill_detail = "\n\n\t---------------------------------------------------------"+"\n\t Current Total: "+str(total_cost)+" Rs.\n\t Previous Due: " + str(prev_due) + "\n\t---------------------------------------------------------\n\t TOTAL DUE : " + str(total_due) + " Rs.\n\t---------------------------------------------------------"
                
                generateBill.add_next_line_to_bill(bill_detail)


                directory = "D:/project/kaalindi app/Invoice/" + str(year) + "/" + str(month) + "/Customer/"
                file_name = str(directory) + str(customer_detail[0]) + " " + str(customer_detail[1]) + ".rtf"
                generateBill.generatebill_to_directory(directory, file_name)
                tkinter.messagebox.showinfo("Succses", "Month Report of " + str(customer_id) + " has been saved :)")
            else:
                tkinter.messagebox.showinfo("Error", "you can only read daily report of a customer in display window.one day report of customer can't be generated. ")

            # generateBill.print_invoice()

        elif str(day) != '' and str(customer_id) == ''  :  #Daily Report
            next_line = "\t\t\t\tDaily Report\n\n"
            next_line += "\tDate:" + str(day) + "/" + str(month) + "/" + str(year) + "\n"
            next_line += "\t-------------------------------------------------------------------\n\tSn_no   Name  \t\t(Shift) \tAmount   Cost\n\t-------------------------------------------------------------------\n"
            generateBill.add_next_line_to_bill(next_line)
            sn_no = 1
            transactions.sort(key=lambda x: x[1])
            
            morning_quantity_sum = 0
            morning_cost_sum = 0
            evening_quantity_sum = 0
            evening_cost_sum = 0

            for transaction in transactions:
                # print(transaction)

                customer_detail_query = "SELECT * FROM customer WHERE id=?"
                customer_detail = self.c.execute(customer_detail_query, (int(transaction[1]),))
                customer_detail = self.c.fetchone()

                date = str(transaction[2]) + "/" + str(transaction[3]) + "/" + str(transaction[4])
                shift = transaction[7][0]
                name = str(customer_detail[0])+" "+customer_detail[1] + " "*int(20-len(customer_detail[1]+str(customer_detail[0])))
                entry = "\t" + str(sn_no)+" "*int(2-len(str(sn_no))) + "       " +name+" "+ str(shift) + "\t" + str(transaction[5]) + " lit.   " + str(transaction[6]) + " Rs."
                sn_no += 1
                generateBill.add_next_line_to_bill(entry)

                if shift == "M":
                    morning_quantity_sum += float(transaction[5])
                    morning_cost_sum += float(transaction[6])
                else:
                    evening_quantity_sum += float(transaction[5])
                    evening_cost_sum += float(transaction[6])


            
            total_liter = morning_quantity_sum + evening_quantity_sum
            total_cost=morning_cost_sum+evening_cost_sum

            end_line = "\n\n\n\t---------------------------------------------------------\n\tMorning Total liter: " + str(morning_quantity_sum) + " \tMorning Total Cost: " + str(morning_cost_sum) + "\n"
            end_line += "\t---------------------------------------------------------\n\tEvening Total liter: " + str(evening_quantity_sum) + " \tEvening Total Cost: " + str(evening_cost_sum) + "\n"
            end_line += "\t---------------------------------------------------------\n\t       Total liter: " + str(total_liter) + "         Total Cost:  " + str(total_cost) + "\n\t---------------------------------------------------------\n"

            generateBill.add_next_line_to_bill(end_line)

            directory = "D:/project/kaalindi app/Invoice/" + str(year) + "/" + str(month) + "/Admin/"
            file_name = str(directory) + str(day)+"-"+str(month)+"-"+str(year)+" daily report" + ".rtf"
            generateBill.generatebill_to_directory(directory, file_name)
            tkinter.messagebox.showinfo("Succses", "Daily report has been saved :)")

            # generateBill.print_invoice()
        elif str(day) == '' and str(customer_id) == '':
            tkinter.messagebox.showinfo("Succses", "one month data of all customers does'nt make sense!!!\n can't print invoice.\nonly visualize transactions.")
            
            
        

            

    def btn_inchange_update_pressed(self, *args, **kwargs):
        # get all entries from change frame
        transaction_id = self.inchange_tran_id_e.get()
        day = self.inchange_day_e.get()
        month = self.inchange_month_e.get()
        year = self.inchange_year_e.get()
        date = str(day) + "-" + str(month) + "-" + str(year)
        customer_id = self.inchange_customer_id_e.get()
        shift = self.inchange_shift.get()
        rate = self.inchange_rate_e.get()
        amount = self.inchange_quantity_e.get()
        # validate
        if day == '' or month == '' or year == '' or shift == '' or customer_id == '' or rate == '' or amount == '':
            tkinter.messagebox.showinfo("Error", "Required Information Missing")
        else:
            
            # focus on current selection
            curr_transaction = self.display_treeview.focus()
            curr_transaction_values = self.display_treeview.item(curr_transaction)['values']
            
            # print(date)
            # print(curr_transaction[3])
            # print(customer_id)
            # print(curr_transaction[1])
            # print(shift)
            # print(curr_transaction[6])
            # print(transaction_id)
            # print(curr_transaction[0])
            
            if str(date) != str(curr_transaction_values[3]) or str(customer_id) != str(curr_transaction_values[1]) or str(shift) != str(curr_transaction_values[6]) or str(transaction_id)!=str(curr_transaction_values[0]):
                tkinter.messagebox.showinfo("Error", "date,customer id, shift, transaction id is changed, please focus on correct row and then try again :(")
            else:
            # pending amount update query
                price = float(rate) * float(amount)
                prev_price = curr_transaction_values[5]

                select_query = "SELECT * FROM customer WHERE id=?"
                cur_customer = self.c.execute(select_query, (customer_id,))
                cur_customer = cur_customer.fetchone()

                pending_amount = float(cur_customer[8]) + price - float(prev_price)

                update_query = "UPDATE customer set pending_amount=? where id=? "
                self.c.execute(update_query, (pending_amount,customer_id,))
                self.conn.commit()

            
            # update query
                update_query = "UPDATE item_transaction set quantity=?,price=? where transaction_id=? AND customer_id=? AND day=? AND month=? AND year=? AND shift=?"
                self.c.execute(update_query, (amount, price,transaction_id,customer_id, day, month, year, shift,))
                self.conn.commit()

                # updates on treeview
                curr_transaction = self.display_treeview.item(curr_transaction, values=(transaction_id, customer_id, curr_transaction_values[2], date, amount, price, shift))

                Message_for_log = "transaction id "+str(transaction_id) +"\n Customer id "+str(customer_id)+"\nhas been succsessfully updated :)"
                self.inlog_tbox.insert(END, ">\n"+Message_for_log+"\n")
            
            # clear all entries
            self.empty_inchange_entries()
        


    def btn_add_new_pressed(self, *args, **kwargs):

        self.add_new_frame.place_forget()
        self.change_frame.place_forget()
        self.add_new_after_retrive_frame.place_forget()
        self.report_frame.place_forget()
        self.update_payment_frame.place_forget()

        self.make_add_new_frame()
        self.add_new_frame.place(x=0, y=0)

    def btn_home_pressed(self, *args, **kwargs):
        self.add_new_frame.place_forget()
        self.change_frame.place_forget()
        self.report_frame.place_forget()
        self.update_payment_frame.place_forget()
        self.add_new_after_retrive_frame.place_forget()
        self.inlog_tbox.delete('1.0',END)
        self.btn_clear_pressed()

    
    def btn_add_all_expected_pressed(self, *args, **kwargs):

        
        day = int(self.day_var.get())
        month = int(self.month_var.get())
        year = int(self.year_var.get())
        if int(day) > 9:
            date = str(day) + "-" + str(month) + "-" + str(year)
        else:
            day = "0" + str(day)
            date = str(day) + "-" + str(month) + "-" + str(year)

        transaction_id_query = "SELECT MAX(transaction_id)  FROM item_transaction"
        cur_transaction_id = self.c.execute(transaction_id_query)
        cur_transaction_id = (cur_transaction_id.fetchone()[0])
        if cur_transaction_id == None:
            cur_transaction_id=int(0)


        customers_query = "SELECT * FROM customer"
        all_customer = self.c.execute(customers_query)
        all_customer = self.c.fetchall()
        treeview_index=0
        self.btn_clear_pressed()
        for customer in all_customer:

            customer_id = customer[0]
            regular_morning_quantity=customer[4]
            regular_morning_rate = customer[5]
            morning_price = regular_morning_quantity*regular_morning_rate
            regular_evening_quantity=customer[6]
            regular_evening_rate = customer[7]
            evening_price = regular_evening_quantity * regular_evening_rate
            pending_amount=customer[8]

            search_query = "SELECT * From item_transaction WHERE customer_id=? AND day=? AND month=? AND year=? AND shift=?"
            
            
            #******* bug he yaha pe , reg 0 he but extra agar add kiya ho alag se toh fir wo db me add ho raha he,
            # display me nai aa raha... - done Solved


            # ***** transaction id 1935 me 1 lit he db me but display me 1.5(regular wala) lit hi dikha raha -done Solved

            already_exists = self.c.execute(search_query, (customer_id, day, month, year, "Morning"))
            already_exists = self.c.fetchall()

            if len(already_exists) != 0:
                for already_exist in already_exists:
                        Treeview_entry = (already_exist[0], already_exist[1], customer[1], date, already_exist[5], already_exist[6], "Morning")
                        self.display_treeview.insert('', 'end', text='', values=Treeview_entry)

            if regular_morning_quantity > 0:
                
                if len(already_exists) == 0:
                    
                    pending_amount = float(morning_price) + float(pending_amount)
                    update_query = "UPDATE customer set pending_amount=? where id=? "
                    self.c.execute(update_query, (pending_amount, customer_id,))
                    self.conn.commit()

                    
                    transaction_query = "INSERT INTO item_transaction (customer_id,day,month,year,quantity,price,shift) VALUES (?,?,?,?,?,?,?)"
                    
                    self.c.execute(transaction_query, (customer_id,day,month,year,regular_morning_quantity, morning_price, "Morning"))
                    
                    # print("morning " + str(customer_id) + " added")
                    cur_transaction_id+=1                
                    Treeview_entry = (cur_transaction_id, customer_id, customer[1], date, regular_morning_quantity, morning_price, "Morning")
                    self.display_treeview.insert('', 'end', text='', values=Treeview_entry)
                    treeview_index += 1
                    

            already_exists = self.c.execute(search_query, (customer_id, day, month, year, "Evening"))
            already_exists = self.c.fetchall()

            if len(already_exists)!=0:
                for already_exist in already_exists:
                    Treeview_entry = (already_exist[0], already_exist[1], customer[1], date, already_exist[5], already_exist[6], "Evening")
                    self.display_treeview.insert('', 'end', text='', values=Treeview_entry)

            if regular_evening_quantity > 0:

                if len(already_exists) == 0:
                    
                    pending_amount = float(pending_amount) + float(evening_price)
                    update_query = "UPDATE customer set pending_amount=? where id=? "
                    self.c.execute(update_query, (pending_amount, customer_id,))
                    self.conn.commit()
                    
                    transaction_query = "INSERT INTO item_transaction (customer_id,day,month,year,quantity,price,shift) VALUES (?,?,?,?,?,?,?)"
                    
                    self.c.execute(transaction_query, (customer_id,day,month,year,regular_evening_quantity, evening_price, "Evening"))
                    # print("evening " + str(customer_id) + " added")
                    cur_transaction_id+=1
                    Treeview_entry = (cur_transaction_id, customer_id, customer[1], date, regular_evening_quantity, evening_price, "Evening")
                    self.display_treeview.insert('', 'end', text='', values=Treeview_entry)
                    treeview_index += 1
                
        Message_for_log = "All expected transaction for date " + str(date) + " has been succsessfully Saved. :)"
        self.inlog_tbox.insert(END, ">\n"+Message_for_log+"\n")
            

            

        self.conn.commit()

    # def log_print(self, *args, **kwargs, message=""):
    #     self.inlog_tbox.insert(END, ">\n"+message+"\n")
    
def make_folder():
    path = "D:\\project\\kaalindi app"
    if not os.path.exists(path):
        os.makedirs(path)
        
if __name__ == "__main__":
    make_folder()
    root = Tk()
    root.configure(bg="gray25")  # EFF7F6
    b = Main(root)
    root.geometry("1366x768+0+0")
    root.resizable(width=0, height=0)
    root.title("Transactions")
    root.mainloop()
