from tkinter import *
from tkinter import messagebox
root=Tk()
w=Label(root,text="Welcome",font="30")
w.pack()
messagebox.showinfo("showinfo","Content")
messagebox.showwarning("showinfo","Warning")
messagebox.showerror("showinfo","Error")

messagebox.askquestion("showinfo","are you sure?")
messagebox.askokcancel("showinfo","Find the output?")
messagebox.askyesno("showinfo","Could you please take this?")
messagebox.askretrycancel("showinfo","Try again?")


root.mainloop()
