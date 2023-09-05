from tkinter import *
from tkinter import ttk
import pymysql



def show():

    root=Tk()

    root.geometry("600x600")
    root.title("Records")

    conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="rms")
    cur = conn.cursor()
    q1= "SELECT * FROM `record`"
    cur.execute(q1)
        
    tree= ttk.Treeview(root,height=30)
    tree['show']='headings'

    tree["columns"]=("Bill","Date","Name","Contact","Amount")
    tree.column("Bill",width=80,minwidth=50,anchor=CENTER)
    tree.column("Date",width=160,minwidth=50,anchor=CENTER)
    tree.column("Name",width=150,minwidth=50,anchor=CENTER)
    tree.column("Contact",width=100,minwidth=50,anchor=CENTER)
    tree.column("Amount",width=100,minwidth=50,anchor=CENTER)



    tree.heading("Bill",text="Bill no.",anchor=CENTER)
    tree.heading("Date",text="Date",anchor=CENTER)
    tree.heading("Name",text="Customer Name",anchor=CENTER)
    tree.heading("Contact",text="Contact Number",anchor=CENTER)
    tree.heading("Amount",text="Amount Paid",anchor=CENTER)


    # vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    # tree.configure(yscrollcommand=vsb.set)

    i=0
    for ro in cur:
        tree.insert("",i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4]))
        i=i+1

    tree.pack()
    # vsb.pack(side=RIGHT, fill=Y)


    root.mainloop()