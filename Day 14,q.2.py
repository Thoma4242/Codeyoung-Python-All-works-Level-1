a=("Apple","Bear")
print(type(a))
b=list(a)
print(type(b))
b.append("Orange")
a=tuple(b)
print(a)