import tkinter as tk 
from tkinter import *
import pyttsx3 

root=Tk()
root.geometry("400x200")
root.resizable(False,False)
root.title("Text to Speech Convertor!")

engine=pyttsx3.init()
textv=StringVar()

def speaknow():
  engine.say(textv.get())
  engine.runAndWait()
  engine.stop()
  
  


obj=LabelFrame(root,text="Text to speech",font=20,bd=1)
obj=Label(fill="both",expand="yes",padx=10,pady=10)

lbl=Label(obj,text="Text",font=30)
lbl.pack(side=tk.LEFT,padx=5)

text=Entry(obj,text="Speak",font=30,width=25,bd=5)
text.pack(side=tk.LEFT,padx=10)

btn=Button(obj,text="Convert",


root.mainloop()
