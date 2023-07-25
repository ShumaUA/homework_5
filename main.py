# i = 0
# while i == 0:
#     try:
#         print("\nEnter the day of the week using numbers from 1 to 7.")
#         user_select = int(input("\nMake your selection: "))
#         match user_select:
#             case 1:
#                 print("\nThe first day of the week is Sunday.")
#             case 2:
#                 print("\nThe second day of the week is Monday.")
#             case 3:
#                 print("\nThe third day of the week is Tuesday.")
#             case 4:
#                 print("\nThe fourth day of the week is Wednesday.")
#             case 5:
#                 print("\nThe fifth day of the week is Thursday.")
#             case 6:
#                 print("\nThe sixth day of the week is Friday.")
#             case 7:
#                 print("\nThe seventh day of the week is Saturday.")
#             case _:
#                 print("\nIncorrect menu number!")
#         print("\nDo you want to continue? [Y]Yes or [N]No.")
#         user_select2 = input("\nMake your selection: ")
#
#         if user_select2 == "Y" or user_select2 == "y":
#             print("\nok let's continue....")
#             i = 0
#         elif user_select2 == "N" or user_select2 == "n":
#             print("\nGood bay!")
#             break
#         else:
#             print("Y or N")
#             i += 1
#         while i != 0:
#             print("\nDo you want to continue? [Y]Yes or [N]No.")
#             user_select2 = input("\nMake your selection: ")
#             if user_select2 == "Y" or user_select2 == "y":
#                 print("\nok let's continue....")
#                 i = 0
#             elif user_select2 == "N" or user_select2 == "n":
#                 print("\nGood bay!")
#                 break
#             else:
#                 print("\nY or N")
#                 i += 1
#
#
#     except ValueError as error:
#         print("\nEnter only integer numbers please!")
#         i = 0


############# hm4_task_1 #############


'''
Користувач вводить рядок з клавіатури.
Порахуйте кількість літер, цифр у рядку. Виведіть обидві кількості на екран. (використовувати цикл)
'''

# text = input("\nEnter text: ")
# Letters, Numbers, Other_symbols = 0, 0, 0
#
# for i in text:
#
#     if i.isalpha():
#         Letters += 1
#
#     elif i.isdigit():
#         Numbers += 1
#
#     else:
#         Other_symbols += 1
#
# print(f"Letters in text: {Letters}, \nNumbers in text: {Numbers}, \nOther symbols in text: {Other_symbols}")


############# hm4_task_2 #############


'''
Користувач вводить з клавіатури рядок та символ для пошуку.
Порахуйте скільки разів у рядку зустрічається потрібний символ. Отримане число виведіть на екран.
'''

# text = input("\nEnter text: ").lower()
# find = input("\nEnter character to search: ").lower()
# print("\nThe desired character occurs:", text.count(find), end=" times")
# print()


############# hm4_task_3 #############


'''
 Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
 Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.
'''

# text = input("\nEnter text: ")
# find = input("\nEnter word to search: ")
# print(f"\nThe desired word '{find}' occurs:", text.count(find), end=" times.")
# print()
#
# old_word = input("\nWhat word should be replaced in the text: ")
# new_word = input("\nEnter new word:")
# print()
#
# print(f"\nAll the words '{old_word}' are replaced by a '{new_word}' .", "\nNew text is: ", text.replace(old_word, new_word))


############# hm4_task_4 #############


'''
Дано рядок. (зробити зрізи)
- Спершу виведіть третій символ цього рядка.
- У другому рядку виведіть передостанній символ цього рядка.
- У третьому рядку виведіть перші п'ять символів цього рядка.
- У четвертому рядку виведіть весь рядок, крім двох останніх символів.
- У п'ятому рядку виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться з першого).
- У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
- У сьомому рядку виведіть усі символи у зворотному порядку.
- У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
- У дев'ятому рядку виведіть довжину цього рядка.
'''

# text = "0123456789"
# print("\n1. The third character of the string is:", text[2], end=".")
# print("\n2. The penultimate character of the string is:", text[-2], end=".")
# print("\n3. The first five characters of the string are:", text[:5], end=".")
# print("\n4. String except for the last two characters is:", text[:-2], end= ".")
# print("\n5. Even characters of this string:", text[::2], end=".")
# print("\n6. Odd characters of this string:", text[1::2], end=".")
# print("\n7. Characters in reverse order of this string:", text[::-1], end=".")
# print("\n8. Characters in reverse order through one of this string:", text[::-2], end=".")
# print("\n9. String length is:", len(text), end=" symbols.")
# print()


############# hm4_task_additional #############


'''
Додатково:
Є певний текст. Реалізуйте наступну функціональність:
■ Змінити текст таким чином, щоб кожне речення починалися з великої літери;
■ Порахуйте скілки разів цифри зустрічаються у тексті;
■ Порахуйте скільки разів розділові знаки зустрічаються в тексті;
■ Порахуйте кількість знаків оклику в тексті.
'''

# import string
# text = "after Arana assumed his new and powerful position, an American embassy official stated in a dispatch that Arana was the type of personality that might assume dictatorial power.\
# on 16 December 1945, Arévalo was seriously injured in a car accident and incapacitated for a period.The leaders of the Revolutionary Action Party (PAR),\
# the party that supported the government, were afraid that Arana would take the opportunity to launch a coup!\
# a handful of its leaders approached Arana and made a deal with him, which later came to be known as the Pacto del Barranco (Pact of the Ravine).\
# arana agreed to refrain from seizing power with the military; in return, the PAR agreed to support Arana's candidacy in the next presidential election, scheduled for November 1950.\
# this undertaking was given in writing! However, it was kept a secret; the American embassy only learned of it in 1947.\
# arévalo himself recovered swiftly, but was forced to support the agreement!"
#
# replaced_text = text.capitalize()
# count_number = sum(i.isdigit() for i in text )
# count_punctuation = sum(i in string.punctuation for i in text)
# count_exclamation_mark = text.count("!")
#
# print(replaced_text)
# print()
#
# print(count_number)
# print()
#
# print(count_punctuation)
# print()
#
# print(count_exclamation_mark)
# print()


############# hm5_task_1 #############


'''
У списку цілих, заповненому випадковими числами обчислити:
■ Суму негативних чисел;
■ Суму парних чисел;
■ Суму непарних чисел;
■ Добуток елементів з кратними індексами 3;
■ Добуток елементів між мінімальним та максимальним елементом;
■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.
'''

##################### v1

# import random
# print()
#
# str = []
# temp_str = []
# sum_negative = 0
# sum_even = 0
# sum_odd = 0
# multi_ix3 = 1
# n1_pos_index = n2_pos_index = 0
# sum_first_end = 0
#
# for i in range(10):
#     str.append(random.randint(-10,10))
# print(f"<-----  list of random numbers  -----> \n{str}")
# print()
#
#
#
# for j in str:
#     if j < 0:
#         sum_negative += j
#
# for j in str:
#     if j % 2 == 0:
#         sum_even += j
#     elif j % 2 != 0:
#         sum_odd += j
#
# for j in str[3::3]:
#     multi_ix3 *= j
#
# for j in range(len(str)):
#     if str[j] > 0:
#         n1_pos_index = j
#         break
#
# for j in range(len(str) -1, -1, -1):
#     if str[j] > 0:
#         n2_pos_index = j
#         break
#
# for i in range(n1_pos_index + 1, n2_pos_index):
#     sum_first_end += str[i]

##################### v2

# import math
# import random
# str = []
#
# for i in range(10):
#     str.append(random.randint(-10,10))
# print(f"<-----  list of random numbers  -----> \n{str}")
# print()
#
# sum_negative = sum(i for i in str if i < 0)
#
# sum_even = sum(i for i in str if i % 2 == 0)
#
# sum_odd = sum(i for i in str if i % 2 != 0)
#
# multi_ix3 = math.prod(str[3::3])
#
# n1 = n2 = 0
# for n1, j in enumerate(str):
#     if j > 0:
#         break
#
# for n2, j in enumerate(reversed(str)):
#     if j > 0:
#         break
#
# sum_first_end = sum(str[n1+1: -n2 -1])


##################################### принты для обеих версий

# print(f"1.The sum of the negative numbers in the list is: {sum_negative}", end=".")
# print(f"\n2.The sum of the even numbers in the list is: {sum_even}", end=".")
# print(f"\n3.The sum of the odd numbers in the list is: {sum_odd}", end=".")
# print(f"\n4.The multiplication of numbers with an index multiple of 3 in the list is: {multi_ix3}", end=".")
# print(f"\n5.The multiplying the maximum and minimum number in the list is: {min(str) * max(str)}", end=".")
# print(f"\n6.The sum of the second and penultimate positive number in the list is: {sum_first_end}", end=".")


############# hm5_task_2 #############


'''
Є список цілих, заповнений випадковими числами.
На підставі даних цього масиву потрібно:
■ Створити список цілих, що містить лише парні числа з першого списку;
■ Створити список цілих, що містить лише непарні числа з першого списку;
■ Створити список цілих, що містить лише негативні числа з першого списку;
■ Створити список цілих, що містить лише позитивні числа з першого списку.
'''

# import random
#
# str = []
# str_even = []
# str_odd = []
# str_negative = []
# str_positive = []
#
# print()
#
# for i in range(20):
#     str.append(random.randint(-50,50))
#
# print(f"<-----  list of random numbers  -----> \n{str}")
# print()
#
#
# for i in str:
#
#     if i % 2 == 0:
#         str_even.append(i)
#     elif i % 2 !=0:
#         str_odd.append(i)
#
# for i in str:
#
#     if i < 0:
#         str_negative.append(i)
#     elif i >= 0:
#         str_positive.append(i)
#
#
# print(f"1.The even numbers in the list is: {str_even}", end=".")
# print(f"\n2.The odd numbers in the list is: {str_odd}", end=".")
# print(f"\n3.The negative numbers in the list is: {str_negative}", end=".")
# print(f"\n4.The positive numbers in the list is: {str_positive}", end=".")


############# hm5_add_task #############


'''
створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99
вивести на екран
- вивести суму чисел головної діагоналі матриці
- вивести мінімальне та максимальне значення побічної діагоналі матриці
- ввести з клавіатури порядковий номер стовпця - вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)
- ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю (аналогічно зробити з рядком)
'''

import random

matrix = []
print()

for i in range(10):
    matrix.append([])
    for j in range(10):
        matrix[i].append(random.randint(10, 99))
print("<--matrix of random numbers-->")

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end=" ")
    print()

sum_main_diag = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i] == matrix[j]:
            sum_main_diag += matrix[i][j]

temp_matrix = []
for i in range(len(matrix) - 1, 0, -1):
    for j in range(len(matrix)):
        if i + j == len(matrix) - 1:
            temp_matrix.append(matrix[i][j])

print("\nWhich column are you interested in?")
n_column_select = int(input("Enter column number from 1 to 10: "))
if n_column_select <= 0 or n_column_select > 10:
    print("\nIncorrect menu number!")

print("\nWhich line are you interested in?")
n_line_select = int(input("Enter line number from 1 to 10: "))
if n_line_select <= 0 or n_line_select > 10:
    print("\nIncorrect menu number!")

numbers_column = []
for i in range(len(matrix)):
    numbers_column.append(matrix[i][n_column_select - 1])

numbers_line = []
for i in range(len(matrix)):
    numbers_line.append(matrix[n_line_select - 1][i])

print(f"\nThe sum of the main diagonal of a matrix is: {sum_main_diag}")

print(f"\nThe minimum value of the secondary diagonal of the matrix is: ", min(temp_matrix))

print(f"\nThe maximum value of the secondary diagonal of the matrix is: ", max(temp_matrix))

print(f"\nNumbers in this column: ", end="")
for i in numbers_column:
    print(i, end=" ")
print()

print(f"\nNumbers in this line: ", end="")
for i in numbers_line:
    print(i, end=" ")
print()


n1_replace_column_select = int(input("\nEnter the first column number to replace from 1 to 10: "))
if n1_replace_column_select <= 0 or n1_replace_column_select > 10:
    print("\nIncorrect menu number!")

n2_replace_column_select = int(input("\nEnter the second column number to replace from 1 to 10: "))
if n2_replace_column_select <= 0 or n2_replace_column_select > 10:
    print("\nIncorrect menu number!")


for i in range(len(matrix)):
    matrix[i][n1_replace_column_select -1], matrix[i][n2_replace_column_select -1] = matrix[i][n2_replace_column_select -1], matrix[i][n1_replace_column_select -1]

print()

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end=" ")
    print()

