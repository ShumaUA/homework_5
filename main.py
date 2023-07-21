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



# import random
# print()
#
# str = []
# temp_str = []
# sum_negative = 0
# sum_even = 0
# sum_odd = 0
# multi_ix3 = 1
# sum_first_end = 0
#
#
# for i in range(10):
#     str.append(random.randint(-10,10))
# print(f"<-----  list of random numbers  -----> \n{str}")
# print()
#
# for j in str:
#
#     if j < 0:
#         sum_negative += j
#     elif j % 2 == 0:
#         sum_even += j
#     elif j % 2 != 0:
#         sum_odd += j
#
# for j in str[3::3]:
#     multi_ix3 *= j
#
# for j in str:
#     if j > 0:
#         temp_str.append(j)
#
# for j in temp_str[1:-1]:
#     sum_first_end += j
#
# if sum_first_end == 0:
#     sum_first_end = "-------->Not enough positive numbers in the list"
#
#
# print(f"1.The sum of the negative numbers in the list is: {sum_negative}", end=".")
# print(f"\n2.The sum of the pair numbers in the list is: {sum_even}", end=".")
# print(f"\n3.The sum of the odd numbers in the list is: {sum_odd}", end=".")
# print(f"\n4.The multiplication of numbers with an index multiple of 3 in the list is: {multi_ix3}", end=".")
# print(f"\n5.The multiplying the maximum and minimum number in the list is: {min(str) * max(str)}", end=".")
# print(f"\n6.The sum of the second and penultimate positive number in the list is: {sum_first_end}", end=".")