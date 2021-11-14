print("Booking for air travel")
destination=["France","England","Spain"]
Class=["Buisness Class","First Class","Economy Class"]
choice=int(input("Enter 1 for Destination \n Enter  2 for Class:"))
if(choice==1):
  b=input("Enter destination:")
  if(b=="France"):
    print("The fare per head is min $4550 ")
  elif(b=="England"):
    print("The fare per head is min $6500")
  elif(b=="Spain"):
    print("The fare  per head is min $2400 ")
  else:
    print("Invalid choice!")
else:
  print("Invalid choice!")
if(choice==2):
  c=input("Enter Class")
  if(c=="First Class"):
    print("The fare per head is min $17200")
  elif(c=="Buisness Class"):
    print("The fare per head is min $10250")
  elif(c=="Economy Class"):
    print("The fare per head is min $2100")
  else:
    print("Invalid Choice!")
else:
  print("Invalid Choice!")
print("This is a program on booking flights to 3 European destiations asking passengers in an online website to enter the destination and the class they want and after they enter that to check how much it costs for them")
