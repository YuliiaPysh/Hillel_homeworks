input_string = input("Enter ")
set_from_string = set(input_string)
unique_symbols = len(set_from_string)

print(unique_symbols)

if unique_symbols > 10:
    print(True)
else:
    print(False)
