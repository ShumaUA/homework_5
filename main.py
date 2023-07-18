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




'''
 Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
 Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.
'''


text = input("\nEnter text: ")
find = input("\nEnter word to search: ")
print(f"\nThe desired word '{find}' occurs:", text.count(find), end=" times.")
print()

old_word = input("\nWhat word should be replaced in the text: ")
new_word = input("\nEnter new word:")
print()

print(f"\nAll the words '{old_word}' are replaced by a '{new_word}' .", "\nNew text is: ", text.replace(old_word, new_word))