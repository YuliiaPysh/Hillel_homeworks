# Task 1

test_string = input("Enter word:")
result_string = ""
counter = 0
while counter < len(test_string):
    if test_string[counter] == 'o' or test_string[counter] == 'O':
        counter += 1
        print("Thank you for entering a word with 'o'.")
        break
    else:
        result_string += test_string[counter]
        counter += 1


# Task 2
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for item in lst1:
    if isinstance(item, str):
        lst2.append(item)
print("String variables:", lst2)


# Task 3
numbers = [1, 2, 4, 5, 6, 7, 23, 345, 21, 56, 89, 34, 111, 9876, 4327, 243, 657, 486]
even_numbers = []
for char in numbers:
    if char % 2 == 0:
        even_numbers.append(char)
print(even_numbers)
print(sum(even_numbers))









