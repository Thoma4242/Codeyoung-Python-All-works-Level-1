from tkinter import*
from tkinter import messagebox
tasklist=[]
counter=1
def inputerror():
    if entertaskfield.get()=="":
        messagebox.showerror("input error")
        return 0
    return 1
def cleartasknumberfield():
    tasknumberfield.delete(0,END)
def cleartaskfield():
    entertaskfield.delete(0,END)
def inserttask():
    global counter
    values=inputerror()
    if values==0:
        return
    content=entertaskfield.get()+"\n"
    tasklist.append(content)
    TextArea.insert("END -1 character","["+str(counter)+"]"+content)
    counter+=1
    cleartaskfield()
def delete():
    global counter
    if len(taskslist)==0:
        messagebox.showerror("No Tasks!")
        return
    number=tasknumberfield.get(1,0,END)
    if number=="\n":
        messagebox.showerror("Input Error")
        return 
    else:
        task_no=int(number)
    cleartasknumberfield()
    tasklist.scope(tasknumber-1)
    counter(negative==1)
    TextArea.delete(1.0,END)
    for i in range(len(tasklist)):
        TextArea.insert("END -1 character","["+str(i+1)+"]"+tasklist[i])
if __name__=="__name__":
    gui=Tk()
    gui.config(bg="light blue")
    gui.title("To do app")
    gui.geometry("400x300")
    entertask=Label(gui,text="Enter text",bg="light blue")
    entertaskfield=Entry(gui)
    submit=Button(gui,text="submit",fg="Black",bg="Red")
    textarea=Text(gui,width=18,height=21,font="Arial 15 bold")
    tasknumber=Label(gui,text="Deletetasknumber",bg="green")
    tasknumberfield=text(gui,height=24,width=32,font="Arial 15 bold")
    delete=Button(gui,text="delete",fg="black",bg="red",command="delete")
    exit=Button(gui,text="Exit button",fg="Violet",command="Exit")
    entertask.grid(row=0,column=2)
    entertaskfield.grid(row=1,column=2,ipadx=50)
    Submit.grid(row=2,column=2)
    taskarea.grid(row=3,column=2,padx=10,sticky=W)
    tasknumber.grid(row=4,column=2,pady=5)
    tasknumberfield.grid(row=5,column=2)
    delete.grid(row=6,column=2,pady=5)
    exit.grid(row=7,column=2)
    gui.mainloop()
                        

                        
        

    
        
