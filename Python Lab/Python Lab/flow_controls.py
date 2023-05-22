thisdict = {"brand":"Ford","model":"Mustang","year":1964}
for x in thisdict:
    print(x)

for x,y in thisdict.items():
    print("items in dict:",x,y)
    
for x in thisdict.values():
    print(x)

for i in range(6):
    print("range value upto 6:",i)

for i in range(2,10):
    print("value start from 2 and end with 10=",i)

for i in range(2,21,2):
    print("values start with 2,end with 20, step is 2=",i)

string="ZEAL"
for i,v in enumerate(string):
    print("loop for string=",v)

