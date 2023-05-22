# Q. Write a Python program to find the sum of all the items in a dictionary.

# dict={"A":10,"B":20,"C":30,"D":40,"E":50}
# print("original dictionary is: ",dict)
# print("sum of dictionary is: ",sum(dict.values()))

dict={"A":10,"B":20,"C":30,"D":40,"E":50}
sum=0
print("original dictionary is: ",dict)
for i in dict.values():
    sum=sum+i
print("sum of dictionary is: ",sum)