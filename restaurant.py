from tkinter import *
import tkinter.messagebox as tmsg 



def login():
    user= uservalue.get()
    pwd= passvalue.get()
    if(user=="shm" and pwd=="shm123"):
        billing_b.config(state=NORMAL)
        tmsg.showinfo("Login","Logged in successful")
    else:
        tmsg.showerror("Invalid Login","PLease Enter valid credentials")
        billing_b.config(state="disabled")
    
    



def reset():
    uservalue.set("")
    passvalue.set("")
    billing_b.config(state="disabled")




def billing():
    root.destroy()
    import billing
    billing.view()
   

root= Tk()
root.geometry("1400x700")
root.title("Shubham Restaurant")
root.configure(bg="#445069")


# ==================restaurant name=================

res_name_l= Label(root,text= "RESTAURANT  MANAGEMENT  SYSTEM",font=('helvetica',25,'bold'),bg="#252B48",relief=GROOVE,bd=6,fg="white",height=2)
res_name_l.pack(side=TOP,fill=X)


# *******************main frame************************

main_frame= Frame(root,bg="#5B9A8B")
main_frame.place(x=290,y=170,width=850,height=400)

# *****************frame items********************

frame_label=Label(main_frame,text="Login",font=('helvetica',20,'bold'),relief=GROOVE,bd=4,width=50,bg="#F7E987")
frame_label.grid(row=0,column=0)

inside_frame=LabelFrame(main_frame,text="Enter details",font=('helvetica',15),relief=GROOVE,bd=5,bg="#96B6C5")
inside_frame.place(x=12,y=60,width=830,height=335)


# =============username and password==============

uservalue= StringVar()
passvalue= StringVar()


username= Label(inside_frame,text="Enter Username",font=('helvetica',12))
username.grid(row=0,column=0,padx=100,pady=10)
user_entry= Entry(inside_frame,textvariable=uservalue,font=('helvetica',12))
user_entry.grid(row=0,column=1)

password= Label(inside_frame,text="Enter Password",font=('helvetica',12))
password.grid(row=1,column=0,padx=100,pady=10)
user_entry= Entry(inside_frame,textvariable=passvalue,font=('helvetica',12),show="*")
user_entry.grid(row=1,column=1)


# ***********************button frame**************************

button_frame= LabelFrame(inside_frame,text="Options",font=('helvetica',12,'bold'),bg="#ADC4CE")
button_frame.place(x=50,y=150,width=700,height=120)

login_b= Button(button_frame,text="Login",font=('Garamond',14,'bold'),width=14,command=login)
login_b.grid(row=0,column=0,padx=34,pady=25)

billing_b= Button(button_frame,text="Billing",font=('Garamond',14,'bold'),width=14,command= billing)
billing_b.grid(row=0,column=1,padx=34,pady=25)
billing_b.config(state="disabled")


reset_b= Button(button_frame,text="Reset",font=('Garamond',14,'bold'),width=14,command=reset)
reset_b.grid(row=0,column=2,padx=34,pady=25)



root.mainloop()
