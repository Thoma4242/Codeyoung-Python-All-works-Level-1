def isPrime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
        return c==2;
a=int(input("Enter the starting range:"))
b=int(input("Ender the ending range:"))
for i in range(a,b+1):
    if isPrime(i):
        print(i)
            
            
          
