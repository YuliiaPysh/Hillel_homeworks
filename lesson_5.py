# from import_example import get_summ, b

# user_word = input("Please enter a word with letter 'O' --> ")
#
# while "o" not in user_word and "O" not in user_word:
#     user_word = input("The letter 'O' is absent in your word, please enter another one --> ")
#
# print(f"Yes, the letter 'О' is present in word '{user_word}'")


# def check_for_letter_o_in_word():
#     user_word = input("Please enter a word with letter 'O' --> ")
#
#     while "o" not in user_word and "O" not in user_word:
#         user_word = input("The letter 'O' is absent in your word, please enter another one --> ")
#
#
# print(f"Yes, the letter 'О' is present in word '{user_word}'")
#
# check_for_letter_o_in_word()
# check_for_letter_o_in_word()


# def get_summ_from_third_numbers(first_number, second_number, third_number=10, *args, **kwargs):
#     print(args)
#     print(kwargs)
#     result = first_number + second_number + third_number
#     return result
#
#
# sum_result = get_summ_from_third_numbers(1, 2, 20)
# sum_result = get_summ_from_third_numbers(1, 2, 20, *[1, 2, 4], **{"k": 13})

# print(sum_result)
#
# def get_summ(*args):
#     return sum(args)
#
# def get_summ_with_tuple(nums_tuple):
#     return sum(nums_tuple)
# print(get_summ_with_tuple((1,2,3,10,100500)))
#
#
# def get_sum_with_kwargs(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#     return sum(kwargs.values())
#
# print(get_sum_with_kwargs(a=2, b=15))

#
# test_list = [1]
# print(test_list)
# def change_zero_element_in_list(list_to_change):
#     list_to_change[0] = 100500
#
# change_zero_element_in_list(test_list)
# print(test_list)
#
#
# a = 0
# def change_number_to_ten(num_to_change):
#     num_to_change = 100500
#
# change_number_to_ten(a)
# print(a)

# from import_example import b, test_func
#
# if __name__ == '__main__':
#     b = [80]
#     test_func()
#     print(id(b))