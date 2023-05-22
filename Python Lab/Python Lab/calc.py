
'''def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b
  
def div(a,b):
    return a/b'''


def operations():
    ch=int(input("enter your choice : "))

    if (ch==1):
        print("addition is : ",add())
           
    elif(ch==2):
        print("substraction is : ",sub())

    elif(ch==3):
        print("multiplication is : ",mul())

    elif(ch==4):
        print("substraction is : ",div())
           
    else:
        print("invalid")
       
def add():
    a=int(input("enter a no: "))
    b=int(input("enter a no: "))
    res=a+b
    return res

def sub():
    a=int(input("enter a no: "))
    b=int(input("enter a no: "))
    res=a-b
    return res

def mul():
    a=int(input("enter a no: "))
    b=int(input("enter a no: "))
    res=a*b
    return res

def div():
    a=int(input("enter a no: "))
    b=int(input("enter a no: "))
    res=a/b
    return res
