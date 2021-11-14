from tkinter import *
from tkinter import messagebox

def login():
  username=entry1.get()
  password=entry2.get()
  if(username=="" and password==""):
    mesagebox.showinfo("","Blank not allowed!")
  elif(username=="Thomas" and password=="thomas"):
    messagebox.showinfo("","login success!")
  elif(userame=="John" and password=="thomas"):
    messagebox.showinfo("","Invalid password!!")
  elif(username=="John" and password=="Abraham"):
    messagebox.showinfo("","login success!")
  else:
    messagebox.showinfo("","Incorrect credentials!")

root=Tk()
root.title("Login")
root.geometry("300x150")
global entry1
global entry2 
Label(root,text="Username").place(x=20,y=20)
Label(root,text="Password").place(x=20,y=70)
entry1=Entry(root,bd=5)
entry1.place(x=140,y=20)
entry2=Entry(root,bd=5)
entry2.place(x=140,y=70)
Button(root,text="Login",command=login,height=3,width=13,bd=6).place(x=100,y=120)

root.mainloop()
