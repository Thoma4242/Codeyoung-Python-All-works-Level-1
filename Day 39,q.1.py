from tkinter import *
class Table:
  def __init__(self,root):
    for i in range(total_rows):
      for j in range(total_columns):
        self.e=Entry(root,width=20,fg="blue",font=("Arial",16,"bold"))
        self.e.grid(row=i,column=j)
        self.e.insert(END,l[i][j])
l=[(1,"Sakshi","Allahabad",22),
  (2,"Thomas","Dubai",16),
  (3,"Abc","Delhi",2),
  (4,"CDf","Mumbai",10)]
total_rows=len(l)
total_columns=len(l[0])
root=Tk()
t=Table(root)
root.mainloop()
