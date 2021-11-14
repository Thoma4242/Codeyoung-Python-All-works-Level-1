d=[30,31,32,33,34]
even_count,odd_count=0,0
for num in d:
    if(num%2==0):
        even_count+=1
    else:
        odd_count+=1
print("Even numbers in the list:",even_count)
print("Odd numbers in the list:",odd_count)
