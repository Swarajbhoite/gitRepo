# Q. Write a Python program to sort a list of tuples in increasing order by the last element in each tuple.

t1=(45,12,26)
t2=(46,8,79,11)
t3=(6,31,3)
t4=(17,26,53)
l=[t1,t2,t3,t4]
print("the list is: ",list)

def last(t):
    l1=len(t)
    return (t[l1-1])
print("Last element of tupel: ",last(t4))
sortlist=sorted(l,key=last)
print("Sorted list: ",sortlist)