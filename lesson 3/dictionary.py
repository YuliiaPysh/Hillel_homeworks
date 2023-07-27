employee_dict = {"testmail@gmail.com": "Test Employee 1",
                 "testmail@gmail.com1": "Test Employee 1",
                  1 : "testemployee"}


print(employee_dict)
print(employee_dict["testmail@gmail.com"])
print(employee_dict[1])
employee_dict[1] = "New Value"
print(employee_dict[1])
print(len(employee_dict))

#dictionaty - ordered/unordered, changeable