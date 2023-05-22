# write a Python program to find maximum of 2 number by using lambda function

# max=lambda x,y : x if (x>y) else y
# print("maximum no is : ",max(10,3))

# min=lambda x,y : x if (x>y) else y
# print("minimum no is : ",min(10,3))

# x=int(input("Enter first no : "))
# y=int(input("Enter second no : "))
# max=lambda x,y : x if (x>y) else y
# print("maximum no is : ",max(x,y))
# print("maximum no is : ",min(x,y))

# write a Python program to find maximum of 3 given numbers by using lambda function

x=int(input("Enter first no : "))
y=int(input("Enter second no : "))
z=int(input("Enter third no : "))
max=lambda x,y,z : x if (x>y and x>z)  else y if (y>x and y>z) else z
min=lambda x,y,z : x if (x<y and x<z)  else y if (y<x and y<z) else z
print("maximum no is : ",max(x,y,z))
print("minimum no is : ",min(x,y,z))

