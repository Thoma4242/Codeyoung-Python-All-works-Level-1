p=int(input("Enter the principle:"))
r=int(input("Enter the rate:"))
n=int(input("Enter the no.of years:"))
c=(p*(1+(r/100))**n)-p
print("The Compound interest is:",c)
