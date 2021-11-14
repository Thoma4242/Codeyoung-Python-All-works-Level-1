s=input("Enter the string:")
d,u,l=0,0,0
for i in s:
    if i.isdigit():
        d+=1
    if i.isupper():
        u+=1
    if i.islower():
        l+=1
print("number of digits:,b")
