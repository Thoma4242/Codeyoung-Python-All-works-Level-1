a=float(input("Enter the 1st num:"))
b=float(input("Enter the 2nd num:"))
choice=int(input("Enter 1 for addition \n Enter 2 for subtraction \n Enter 3 for Multiplication \n Enter 4 for Division \n Enter 5 for remainder:"))
if(choice==1):
    print("Sum:",a+b)
elif(choice==2):
    print("difference:",a-b)
elif(choice==3):
    print("product:",a*b)
elif(choice==4):
    print("Division:",a/b)
elif(choice==5):
    print("Remainder:",a%b)
else:
    print("Invalid choice!")
