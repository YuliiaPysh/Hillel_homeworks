counter = 1

#  while counter <= 10:
#      print(counter)
#      counter += 1

while True:
    print(counter)
    if counter >= 10:
        break
    counter += 1


test_string = "asd vbn"
result_string = ""
counter = 0
while counter < len(test_string):
    if test_string[counter] == ' ':
        counter += 1
        continue
    else:
        result_string += test_string[counter]
        counter += 1
print(result_string)


