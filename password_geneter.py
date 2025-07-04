from tkinter import *
from random import randint
ps=Tk()
ps.title("Password Generator")
ps.geometry("800x600")
ps.iconbitmap("H:/CODESOFT TASK/shiva.jpg")

my_password=chr(randint(33,126))
def rand():
    global pw_length
    global lab1
    pw_entry.delete(0,END)
    pw_length=int(my_entry.get())
    if(pw_length<=0):
        lab1=Label(ps,text="Enter greater value than 1")
        lab1.grid(row=6,column=0)
    my_password=""
    for x in range(pw_length):
        my_password +=chr(randint(33,126))
    pw_entry.insert(0,my_password)
def accept():
    global lab
    if(pw_length<=0):
        lab=Label(ps,text="Not accepted reset again.",bg="red")
        lab.grid(row=6,column=0)
    else:
        lab=Label(ps,text="Your password accepted.",bg="light green")
        lab.grid(row=6,column=0)
def reset():
    my_entry.delete(0,END)
    pw_entry.delete(0,END)
    user_name.delete("0","end")
    lab.after(1000,lab.destroy())
    
label1=Label(ps,text="Enter User name:")
label1.grid(row=0,column=0)

user_name=Entry(ps)
user_name.grid(row=0,column=1,padx=20)


label2=Label(ps,text="Enter password length:")
label2.grid(row=1,column=0,pady=30)

my_entry=Entry(ps)
my_entry.grid(row=1,column=1,padx=20,pady=30)


label3=Label(ps,text="Generated password:")
label3.grid(row=2,column=0)

pw_entry=Entry(ps,text=" ")
pw_entry.grid(row=2,column=1)

gen_button=Button(ps,text="GENERATE PASSWORD",command=rand)
accept_button=Button(ps,text="ACCEPT",command=accept)
reset_button=Button(ps,text="RESET",command=reset)
gen_button.grid(row=3,column=3,pady=15)
accept_button.grid(row=4,column=3,pady=5)
reset_button.grid(row=5,column=3,pady=5)

mainloop()


