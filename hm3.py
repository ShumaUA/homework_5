'''
Користувач вводить із клавіатури номер дня тижня (1-7).
Необхідно вивести на екран назви дня тижня.
Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.
'''

# Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday

# while True:
#     print("Enter the day of the week using numbers from 1 to 7.")
#     try:
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
#                 print("\nDo you want to continue? [Y]Yes or [N]No.")
#                 user_select2 = input("\nMake your selection: ")
#                 if user_select2 == "Y" or user_select2 == "y":
#                     print("ok let's continue....")
#                 elif user_select2 == "N" or user_select2 == "n":
#                     print("Good bay!")
#                     break
#
#     except ValueError as error:
#         print("\nEnter only integer numbers please!")




'''
Користувач вводить два числа.
Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання.
'''


# while True:
#     try:
#         n1 = float(input("Input first number: "))
#         n2 = float(input("Input second number: "))
#         if n1 == n2:
#             print(f"\nThe number {n1} is equal to the number {n2}")
#         elif n1 > n2:
#             print(f"\n{n2}, {n1}")
#         elif n1 < n2:
#             print(f"\n{n1}, {n2}")
#     except ValueError as error:
#         print("Enter numbers please!")
#     ask = input("\nEnter [N] to break or press any key to continue...\nYour choice :")
#     if ask == "N" or ask == "n":
#         print("Good bay!")
#         break



'''
Користувач вводить два числа та матем дію: + - * або /
Залежно від введеної матем дії вивести результат

'''

# while True:
#
#     try:
#
#         n1 = float(input("Input first number: "))
#         n2 = float(input("Input second number: "))
#         print("Select an action\n[1] for summation, [2] for subtraction, [3] for multiplication, [4] for division.")
#         ask = int(input("Your select?: "))
#
#         match ask:
#             case 1:
#                 r1 = n1 + n2
#                 print(f"\nThe summation of the numbers is: {r1}")
#             case 2:
#                 r2 = n1 - n2
#                 print(f"\nThe subtracting numbers is: {r2}")
#             case 3:
#                 r3 = n1 * n2
#                 print(f"\nThe multiplication numbers is: {r3}")
#             case 4:
#                 r4 = n1 / n2
#                 print(f"\nThe division numbers is: {r4}")
#             case _:
#                 print("\nIncorrect menu number!")
#
#     except ValueError as error:
#         print("Enter numbers please!")
#     except ZeroDivisionError as error:
#         print("Division by 0 is not possible.")
#
#     ask = input("\nEnter [N] to break or press any key to continue...\nYour choice :")
#     if ask == "N" or ask == "n":
#         print("Good bay!")
#         break
