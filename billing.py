from tkinter import *
import random
from datetime import datetime
from tkinter import filedialog
import pymysql
import tkinter.messagebox as tmsg 


grand_total=0

# +++++++++++++++++++++functions++++++++++++++++++++++++

def default_bill():
    textarea.insert(END,"\t\t\t     SHUBHAM RESTAURANT")
    textarea.insert(END,"\n\t\t               Schobee Street,Bidhan Nagar")
    textarea.insert(END,"\n\t\t\t        Contact:- 7367454577")
    textarea.insert(END,"\n=====================================================================")
    # if randomnum== billnum.get():
    #     textarea.insert(END,f"\nBill Number : {billnum.get()}")


def genbill():
    textarea.insert(END,f"\nBill Number : {billnum.get()}")
    textarea.insert(END,f"\nCustomer Name : {name.get()}")
    textarea.insert(END,f"\nPhone Number : {phone.get()}")
    textarea.insert(END,f"\nDate : {date_pr.get()}")
    textarea.insert(END,"\n=====================================================================")
    textarea.insert(END,"\nProduct Name\t\t\tQuantity\t\t\tCost per item\t\t\tTotal")
    textarea.insert(END,"\n=====================================================================")
    add_bt.config(state=NORMAL)
    reset_bt.config(state=NORMAL)
    clear_bt.config(state=NORMAL)
    item.config(state=NORMAL)
    itementry.config(state=NORMAL)  
    item_qty.config(state=NORMAL)
    item_qtyentry.config(state=NORMAL)
    cost_of_1.config(state=NORMAL)
    cost_of_1entry.config(state= NORMAL)


def add():
    
    global grand_total
    textarea.insert(END,f"\n{itemname.get()}\t\t\t{quantity.get()}\t\t\t{perprice.get()}")
    total= quantity.get()*perprice.get()
    textarea.insert(END,f"\t\t\t{total}")
    grand_total+= total
    total_bt.config(state=NORMAL)
    save_bt.config(state=NORMAL)
    

def clear():
    itemname.set("")
    quantity.set("")
    perprice.set("")
 


def reset():
    textarea.delete("1.0",END)
    default_bill()
    itemname.set("")
    quantity.set("")
    perprice.set("")
    name.set("")
    phone.set("")
    randomnum1= random.randint(101,9999)
    billnum.set(randomnum1)
    # textarea.insert(END,f"\nBill Number : {billnum.get()}")

    total_bt.config(state=DISABLED)
    save_bt.config(state=DISABLED)
    clear_bt.config(state=DISABLED)
    add_bt.config(state=DISABLED)
    item.config(state=DISABLED)
    itementry.config(state=DISABLED)
    item_qty.config(state=DISABLED)
    item_qtyentry.config(state=DISABLED)
    cost_of_1.config(state=DISABLED)
    cost_of_1entry.config(state= DISABLED)


def total():
   
    textarea.insert(END,"\n=====================================================================")
    textarea.insert(END,f"\n\t\t\t\t\t\t\t       Grand Total : {grand_total}")



def save():
  
    try:

        conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="rms")
        cur = conn.cursor()

        bill = billnum.get()
        cn = name.get()
        cno = phone.get()

        q1 = "INSERT INTO `record` (`Bill no`, `Customer Name`, `Contact no`,`Amount paid`) VALUES (%s, %s, %s, %s)"
        values = (bill, cn, cno,grand_total)

        res = cur.execute(q1, values)

        if res:
            conn.commit()
            conn.close()
            print("Data inserted successfully")
        else:
            print("Data insertion failed")

    except Exception as e:

        print("Connection error:", e)



    bill_content = textarea.get("1.0", END)
    
    # Prompt the user to choose a file location for saving
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    
    if file_path:
        with open(file_path, "w") as file:
            file.write(bill_content)

    tmsg.showinfo("Message","Bill successfully saved!")


def selling():
        import record
        record.show()

    


def view():
    global textarea
    global total_bt
    global save_bt
    global add_bt
    global reset_bt
    global clear_bt
    global billnum
    global itemname
    global itementry
    global item_qtyentry
    global quantity
    global perprice
    global item
    global item_qty
    global cost_of_1
    global cost_of_1entry
    global name
    global phone
    global date_pr
    root= Tk()
    root.geometry("1200x730")
    root.title("Shubham Restaurant")
    root.configure(bg="#445069")



    # ==================restaurant name=================

    res_name_l= Label(root,text= "RESTAURANT  MANAGEMENT  SYSTEM",font=('helvetica',25,'bold'),bg="#252B48",relief=GROOVE,bd=6,fg="white",height=2)
    res_name_l.pack(side=TOP,fill=X)


    # *************************frame 1********************

    # ****************variables**********************
    global randomnum
    randomnum= random.randint(100,9999)
    #random number generator for bill no

    billnum=IntVar()
    billnum.set(randomnum)
    name=StringVar()
    phone = StringVar()
    itemname= StringVar()
    quantity=IntVar()
    perprice= IntVar()
    date_pr= StringVar()
    date_pr.set(datetime.now())


    frame1= LabelFrame(root,text="Enter details",font=('helvetica',15,'bold'),bg="#5B9A8B")
    frame1.place(x= 90,y=120,width=400,height=558)

    bill_no= Label(frame1,text="Bill Number",font=('helvetica',13),bg="#5B9A8B")
    bill_no.grid(row=0,column=0,padx=40,pady=10)
    bill_entry= Entry(frame1,textvariable=billnum,font=('helvetica',12))
    bill_entry.grid(row=0,column=1)
    bill_entry.config(state=DISABLED)



    date= Label(frame1,text="Date",font=('helvetica',13),bg="#5B9A8B")
    date.grid(row=1,column=0,padx=40,pady=10)
    dateentry= Entry(frame1,textvariable=date_pr,font=('helvetica',12))
    dateentry.grid(row=1,column=1)




    cust_name= Label(frame1,text="Customer Name",font=('helvetica',13),bg="#5B9A8B")
    cust_name.grid(row=2,column=0,padx=40,pady=10)
    cust_nameentry= Entry(frame1,textvariable=name,font=('helvetica',12))
    cust_nameentry.grid(row=2,column=1)



    cont_no= Label(frame1,text="Contact Number",font=('helvetica',13),bg="#5B9A8B")
    cont_no.grid(row=3,column=0,padx=40,pady=10)
    cont_noentry= Entry(frame1,textvariable=phone,font=('helvetica',12))
    cont_noentry.grid(row=3,column=1)



    item= Label(frame1,text="Item Purchased",font=('helvetica',13),bg="#5B9A8B")
    item.grid(row=4,column=0,padx=40,pady=10)
    itementry= Entry(frame1,textvariable=itemname,font=('helvetica',12))
    itementry.grid(row=4,column=1)
    item.config(state=DISABLED)
    itementry.config(state=DISABLED)





    item_qty= Label(frame1,text="Item quantity",font=('helvetica',13),bg="#5B9A8B")
    item_qty.grid(row=5,column=0,padx=40,pady=10)
    item_qtyentry= Entry(frame1,textvariable=quantity,font=('helvetica',12))
    item_qtyentry.grid(row=5,column=1)
    item_qty.config(state=DISABLED)
    item_qtyentry.config(state=DISABLED)




    cost_of_1= Label(frame1,text="Cost of one",font=('helvetica',13),bg="#5B9A8B")
    cost_of_1.grid(row=6,column=0,padx=40,pady=10)
    cost_of_1entry= Entry(frame1,textvariable=perprice,font=('helvetica',12))
    cost_of_1entry.grid(row=6,column=1)
    cost_of_1.config(state=DISABLED)
    cost_of_1entry.config(state= DISABLED)




    # *********************option frame********************

    opt_frame= LabelFrame(frame1,text="Options",font=('helvetica',15,'bold'))
    opt_frame.place(x= 8,y=310,width=380,height=210)

    add_bt=Button(opt_frame,text="Add",font=('Garamond',14,'bold'),width=8,command=add)
    add_bt.grid(row=0,column=0,padx=10,pady=15)
    add_bt.config(state=DISABLED)


    gen_bt=Button(opt_frame,text="Generate",font=('Garamond',14,'bold'),width=8,command=genbill)
    gen_bt.grid(row=0,column=1,padx=10,pady=15)

    clear_bt=Button(opt_frame,text="Clear",font=('Garamond',14,'bold'),width=8,command=clear)
    clear_bt.grid(row=0,column=2,padx=10,pady=15)
    clear_bt.config(state=DISABLED)


    total_bt=Button(opt_frame,text="Total",font=('Garamond',14,'bold'),width=8,command=total)
    total_bt.grid(row=1,column=0,padx=10,pady=15)
    total_bt.config(state=DISABLED)


    save_bt=Button(opt_frame,text="Save",font=('Garamond',14,'bold'),width=8,command=save)
    save_bt.grid(row=1,column=1,padx=10,pady=15)
    save_bt.config(state=DISABLED)


    reset_bt=Button(opt_frame,text="Reset",font=('Garamond',14,'bold'),width=8,command=reset)
    reset_bt.grid(row=1,column=2,padx=10,pady=15)
    reset_bt.config(state=DISABLED)

    tot_selling=Button(opt_frame,text="Total Selling",font=('Garamond',14,'bold'),command=selling)
    tot_selling.grid(row=2,column=1,padx=10,pady=1)



    # *************frame2****************


    def click(event):
        text= event.widget.cget("text")
        if text=="=":
            if scvalue.get().isdigit():
                value=int(scvalue.get())
            else:
                value= eval(screen.get())
            scvalue.set(value)
            screen.update()
            
        elif text=="AC":
            scvalue.set("")
            screen.update()
            
        else:
            scvalue.set(scvalue.get() + text)
            screen.update()
        




    scvalue=StringVar()
    scvalue.set("")

    frame2= Frame(root,relief=GROOVE,bd=5)
    frame2.place(x= 560,y=120,width=590,height=300)

    screen= Entry(frame2,textvariable=scvalue,font=('helvetica',25),justify='right',width=32,relief=GROOVE,bd=3)
    screen.grid(row=0,column=0,columnspan=30)


    b7= Button(frame2,text="7",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    b7.grid(row=1,column=0,padx=2)
    b7.bind("<Button-1>",click)

    b8= Button(frame2,text="8",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    b8.grid(row=1,column=1,padx=2)
    b8.bind("<Button-1>",click)

    b9= Button(frame2,text="9",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    b9.grid(row=1,column=2,padx=2)
    b9.bind("<Button-1>",click)

    bplus= Button(frame2,text="+",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    bplus.grid(row=1,column=3)
    bplus.bind("<Button-1>",click)




    b4= Button(frame2,text="4",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    b4.grid(row=2,column=0,)
    b4.bind("<Button-1>",click)

    b5= Button(frame2,text="5",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    b5.grid(row=2,column=1)
    b5.bind("<Button-1>",click)
    b6= Button(frame2,text="6",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    b6.grid(row=2,column=2)
    b6.bind("<Button-1>",click)
    bsub= Button(frame2,text="-",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    bsub.grid(row=2,column=3)
    bsub.bind("<Button-1>",click)


    b1= Button(frame2,text="1",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    b1.grid(row=3,column=0,)
    b1.bind("<Button-1>",click)

    b2= Button(frame2,text="2",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    b2.grid(row=3,column=1)
    b2.bind("<Button-1>",click)

    b3= Button(frame2,text="3",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    b3.grid(row=3,column=2)
    b3.bind("<Button-1>",click)

    bmul= Button(frame2,text="*",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    bmul.grid(row=3,column=3)
    bmul.bind("<Button-1>",click)



    b0= Button(frame2,text="0",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    b0.grid(row=4,column=0,)
    b0.bind("<Button-1>",click)

    b00= Button(frame2,text="00",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    b00.grid(row=4,column=1)
    b00.bind("<Button-1>",click)

    bclear= Button(frame2,text="C",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    bclear.grid(row=4,column=2)
    bclear.bind("<Button-1>",click)

    bdiv= Button(frame2,text="/",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    bdiv.grid(row=4,column=3)
    bdiv.bind("<Button-1>",click)



    bpoint= Button(frame2,text=".",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    bpoint.grid(row=5,column=0,)
    bpoint.bind("<Button-1>",click)

    bper= Button(frame2,text="AC",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    bper.grid(row=5,column=1)
    bper.bind("<Button-1>",click)

    bequal= Button(frame2,text="=",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    bequal.grid(row=5,column=2)
    bequal.bind("<Button-1>",click)

    bdiv= Button(frame2,text="%",font=('helvetica',17),width=10,height=1,relief=GROOVE,bd=3)
    bdiv.grid(row=5,column=3)
    bdiv.bind("<Button-1>",click)


    # **************frame3***************

    frame3= LabelFrame(root,text="Billing Area",relief=GROOVE,bd=5,font=('helvetica',15,'bold'))
    frame3.place(x= 560,y=430,width=590,height=250) 

    y_scroll= Scrollbar(frame3,orient="vertical")
    textarea= Text(frame3,yscrollcommand=y_scroll.set)
    y_scroll.pack(side= RIGHT,fill=Y)
    y_scroll.config(command=textarea.yview)
    textarea.config(font=('lucida',10,'bold'))
    textarea.pack(fill= BOTH,expand=TRUE)
    default_bill()



    root.mainloop()


# view()