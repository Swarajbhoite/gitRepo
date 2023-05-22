# Q Write a Python program to count the number of lowercase characters and uppercase characters in a string.

n=input("Enter String: ")
upper=0
lower=0
for i in n:
    if (i.islower()):
        lower=lower+1
    elif (i.isupper()):
        upper=upper+1
print("lower characters = ",lower)
print("upper characters = ",upper)