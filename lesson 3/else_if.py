first_num = int(input("Enter first number "))
second_num = int(input("Enter second name "))

if first_num > second_num:
    print(True)
    print("first number more than second")
elif first_num < second_num:
    print(False)
    print("second number more than first")
else:
    print("Equal")