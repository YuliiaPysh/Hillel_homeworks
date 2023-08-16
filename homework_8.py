# Version1
def number_range(count):
    num = 1
    while num <= count:
        yield num
        num += 1


for el in number_range(9):
    print(el)

print("*==================*")


# Version2
def number_generator(start, end):

    while start <= end:
        yield start
        start += 1


for y in number_generator(1, 9):
    print(y)
