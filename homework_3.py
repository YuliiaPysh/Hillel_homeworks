input_string = input("Enter ")
set_from_input = set(input_string)
unique_symbols = len(set_from_input)
print(unique_symbols)

if unique_symbols > 10:
    print(True)
else:
    print(False)