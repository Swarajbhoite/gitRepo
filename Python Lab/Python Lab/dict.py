# write a program to create dictionary for storing information about university.

dict={"University Name":"Savitribai Phule Pune University",
	"Address":"Ganeshkhind Rd, Ganeshkhind, Pune, Maharashtra 411007",
	"Phn No":"1234567890"}
print(dict)
print("dictionary type=",type(dict))
print("get items=",dict.items())
print("get particular value=",dict.get("Address"))

l1=dict.items()
print ("values of l1=",l1)

Dict1={"A":"Greeks","B":"for",}
Dict2={"C":"Greeks"}
print("original dictionary: ",Dict1)
Dict1.update(Dict2)
print("updated dictionary=",Dict1)
pop=Dict1.pop("C")
print("after pop=",Dict1)