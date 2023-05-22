# factorial using for loop

# n = 23
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print("The factorial of 23 is : ", end="")
# print(fact)

# factorial using if_else

## num = 7
## To take input from the user
# num = int(input("Enter a number: "))
# factorial = 1
# ## check if the number is negative, positive or zero
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)

# factorial using function
def factorial(x):
    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))
num = 7
result = factorial(num)
print("The factorial of", num, "is", result)
