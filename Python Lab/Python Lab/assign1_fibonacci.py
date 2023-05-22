# Q Write a Python program to print fibonacci series of n terms.

x=0
y=1
n=int(input("enter no:"))
if n>0:
    print(x)
    print(y)

    for i in range(1,n+1):
        z=x+y
        print(z," ")
        x=y
        y=z
else:
    print("Please enter greater number than 0")