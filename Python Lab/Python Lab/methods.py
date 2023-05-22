list=[1,23,432,234]
print("Original list is:",list)

list.append(3)
print("append list is:",list)

list.copy()
print("copy list is:",list)

list.reverse()
print("reverse of list",list)

list.pop(2)
print("after pop 2 index:",list)

n=list.count(1)
print("count of 1 is:",n)