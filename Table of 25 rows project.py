from tkinter import*
class Table:
 def_init_(self,root): 
   for i in range(total_rows):
     for j in range(total_columns):
        self.e=Entry(root,width=20,fg="Blue")
        font=("Arial",16,"Bold")
        self.grid(row=i,column=j)
        self.insert(END,l[i],[j])
l=[(1,"Sakshi Maam","Allahabad",22),
   (2,"Thomas","Dubai",16),
   (3,"ABC","Delhi",2),
   (4,"CDE","Mumbai",10),
   (5,"EFG","Tokyo",22),
   (6,"HIJ","Bangalore",24),
   (7,"OPQ","Kolkata",26),
   (8,"RST","Trivandrum",28),
   (9,"UVW","Naya Raipur",30),
   (10,"XYZ","Rajkot",42),
   (11,"James","Amaravati",44),
   (12,"Charles","Patna",42),
   (13,"Jimmmy","Karimnagar",50),
   (14,"John","Muzzafarpur",8),
   (15,"Liam","Puducherry",9),
   (16,"Noah","Dehradun",10),
   (17,"Oliver","Tirupur",11),
   (18,"Elijah","Billaspur",12),
   (19,"William","Pallisgarh",16),
   (20,"Benjamin","Aligarh",17),
   (21,"Lucas","Gangtok",22),
   (22,"Henry","Paris",63),
   (23,"Alexander","Berlin",64),
   (24,"Krishna","Beirut",72),
   (25,"Hanuman","Ettumanoor",81)]
total_rows=len(1)
total_columns=len(l[0])
root=Tk()
t=Table(Root)
root.mainloop()

   
