f=open("demo.txt","w")
r="This is the 1st record"
for i in range(0,6):
    f.write(r)
f.close()
f=open("kvpy.txt","w")
a="This is the 2nd record"
for i in range(0,6):
    f.write(a)
f.close()
f=open("ke.txt","w")
b="This is the 3rd record"
for i in range(0,6):
    f.write(b)
f.close()
