with open("data.txt", "x") as file:
    file.write("123\n")
    file.write("33\n")
    file.write("645\n")

numbers = [123, 33, 645]
summ = sum(numbers)
print(summ)

with open("data.txt", "r") as file:
    result = file.readlines()

result_array = []
for r in result:
    try:
        result_array.append(r.replace("\n", ''))
    except AttributeError:
        print("Attribute error")
    except ValueError:
        print("Value error")

print(result_array)
