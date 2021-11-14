a=["Toy","Mango","Tool","Odd"]
def swaplist(a):
    a[0],a[-1]=a[-1],a[0]
    return a
print(swaplist(a))
