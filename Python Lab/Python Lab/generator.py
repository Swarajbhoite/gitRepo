# def my_generator(n):
#     value=0
#     while value < n :
#         yield value
#         value += 1
# for value in my_generator(4):
#     print(value)

# create the generator object
# squares_generator = (i * i for i in range(6))
# # iterate over the generator and print the values
# for i in squares_generator:
#     print(i)


def generator():
    for i in range(10):
        if (i%2==0):
            yield (i*i)
        else:
            yield(i)
print("Output : ")
for i in generator():
    print(i)