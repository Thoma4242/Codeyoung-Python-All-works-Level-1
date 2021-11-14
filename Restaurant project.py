print("Welcome to the Restaurant suggestion app")
location=["Bur Dubai","Qusais","Ras al Khor"]
print(location)
l=int(input("Enter the location of your choice:\n Enter 1 for Bur Dubai \n Enter 2 for Qusais \n Enter 3 for Ras al Khor:"))
restaurant=["Pizzahut","KFC","Calicut paragon"]
print(restaurant)
choice=int(input("Enter your choice:\nEnter 1 for BurDubai\nEnter 2 for KFC\nEnter 3 for Calicut paragon:"))
if(l==1):           
    if(choice==1):
     print("Overall Rating=4.6")
     print("Ambience=Excellent")
     print("Distance is 12 Km")
     print("Mode of travel-Car")
    elif(choice==2):
     print("Overall Rating=4.2")
     print("Ambience=Excellent")
     print("Distance is 20 Km")
     print("Mode of travel-Car")
    elif(choice==3):
     print("Overall Rating=3.6")
     print("Ambience=Very Good")
     print("Distance is 45 Km")
     print("Mode of travel-Car or train")
    else:
     print("Invalid choice!")

