n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
n3=int(input("Enter number 3:"))
if((n1>n2) and (n1>n3)):
    print(n1,"is the largest among the 3 numbers")
elif((n2>n1) and (n2>n3)):
    print(n2,"is the largest among 3 numbers")
elif((n3>n1) and (n3>n2)):
    print(n3,"is the largest among 3 numbers")
else:
    print("These numbers are equal")
    
