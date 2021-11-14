ini_string='abcdef'
c=="b"
print("initial string:",ini_string,"\n character_to_find:",c)
res=None
for i in range(0,len(ini_string)):
    if ini_string[i]==c:
        res=i+1
        break
if res==None:
    print("No such character available in string")
else:
    print("character{}is present at {}".format(c,str(res)))
