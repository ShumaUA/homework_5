# num5 = 111
# num1 = 12
# num2 = 15
# num3 = 16
# num4 = 17
# print(num1)
# print(num2)
# print(num3)
# print(num4)
# print(num5)

# num = 10
#
# if num == 5:
#     print(num)

# if 10:
#     print("ok")
#
#
# if '10':
#     print("ok")
#
# if 0:
#     print("ok")

###############
#
# for i in range(5):  # 0 1 2 3 4
#     # print("Hello")
#     print(i, end=" ")
#
# print()
#
# for i in range(2, 5):
#     # print("Hello")
#     print(i, end=" ")
#
# print()
#
# for i in range(1, 5, 2):
#     # print("Hello")
#     print(i, end=" ")
#
# print()
#
# start, end = 1, 10
# for i in range(start, end + 1):
#     print(i, end=" ")
#
# print()
#
# start, end = 1, 10
# for i in range(start, end + 1, 2):
#     print(i, end=" ")
#
# print()
#
# start, end = 2, 10
# for i in range(start, end + 1, 2):
#     print(i, end=" ")
#
# print()
#
# start, end = 1, 10
# for i in range(end, start - 1, -1):
#     # print("Hello")
#     print(i, end=" ")

########
# for i in range(1, 5):
#     for _ in range(i):
#         print("*", end=" ")
#     print()

####
# HEIGHT = 10
# WIDTH = 10
# whitespaces = 0
# stars = 10
#
# for i in range(HEIGHT):
#     for _ in range(whitespaces):
#         print("  ", end="")
#     for _ in range(stars):
#         print("* ", end="")
#     whitespaces += 1
#     stars -= 1
#
#     print()

# так нельзя делать потому что непонятно что хранит эта переменная, название переменной должно
# описывать тот контент который она хранит
# _ = "Vasya"
# print(_)

####
# Показати на екран усі прості числа в діапазоні, вказаному користувачем.
# Число називається простим, якщо воно ділиться без залишку тільки на себе і на одиницю.
# Наприклад, три - це просте число, а чотири - ні.

# start = int(input("Enter start value: "))
# end = int(input("Enter end value: "))
#
# # v1 (swap)
# if start > end:
#     start, end = end, start
#
# # v2
# # if start > end:
# #     temp = start
# #     start = end
# #     end = temp
#
# for number in range(start, end + 1):
#     is_simple = True
#
#     if number < 2:
#         continue
#
#     for i in range(2, number):
#         if number % i == 0:  # якщо залишок вiд дiлення дорiвнюе нулю - число не простое
#             is_simple = False
#             break
#
#     if is_simple:
#         print(number, end=" ")

############
# message = "hello world"
# message_1 = 'hello ' \
#             'world'
# print(message)
#
# text = ("hello"
#         "world")
# print(text)
#
# # raw строка
# text = '''
# qwerrty
#     asdfadsvf
#         asdvsvb
# '''
#
# print(text)
#
# # v1
# path = r"C:\Users\admin\PycharmProjects\FastAPI_materials"
# print(path)
# # v2
# path = "C:\\Users\\admin\\PycharmProjects\\FastAPI_materials"
# print(path)
#
# #
# print("hello, \"world\"\n\tfrom program")
#
# name, surname = "Vasya", "Pupkin"

###
#
# dogs, cats = 12, 15
# result = f"Dogs {dogs} and cats {cats}"
# print(result)
#
# result = "Dogs {} and cats {}".format(dogs, cats)
# print(result)
#
# result = "Dogs {1} and cats {0}".format(dogs, cats)
# print(result)
#
# result = "Dogs {1} and cats {1}".format(dogs, cats)
# print(result)

##########
###
# message = "hello world"
# # [] -> індексатори
# # Індекс - це порядковий номер елемента в колекції (масиві). Note: не всі колекції підтримують індекси.
# # Індекси рахуються з нуля
# print(message[0])
# print(len(message))  # кількість символів у рядку
# # print(message[len(message)])  # IndexError: string index out of range
# print(message[len(message) - 1])
# print(message[-1])

############
###
# # string - immutable тип даних, рядок змінити не можна
# name = "Petya"
# print(name)
# # name[1] = "r"  # TypeError: 'str' object does not support item assignment
# user_name = "Vasya"
# name = user_name
# print(name)

# # v1
# sentence = "Hello, world"
# for letter in sentence:
#     print(letter, end=" ")
#
# print()
#
# # v2
# for i in range(len(sentence)):
#     print(sentence[i], end=" ")

# slices (срезы)
# sentence = "Hello, world"
# print(sentence[:])
# print(sentence[0:])
# print(sentence[2:])
# print(sentence[2:8])
# print(sentence[1:10:2])
# print(sentence[::-1])

###
#
# name = "Vasya"
# surname = "Petrov"
# age = 33
#
# fullname = name + " " + surname + " " + str(age)  # конкатенація (додавання рядків)
# print(fullname)

#
# text = "Hello, world" * 3
# print(text)
#
# print("---" * 10)
#
# a1 = "abc"
# a2 = "abs"
#
# if a1 > a2:
#     print(a1)
# else:
#     print(a2)
#
# print(ord("A"))
# print(chr(98))
# print(ord('b'))

###############
####
# text = "helLo woRlD"

# # isalpha(): повертає True, якщо рядок складається лише з алфавітних символів
#
# print(text.isalpha())
#
# # islower(): повертає True, якщо рядок складається лише із символів у нижньому регістрі
#
# print(text.islower())
#
# # isupper(): повертає True, якщо всі символи рядка у верхньому регістрі
#
# print(text.isupper())
#
# # isdigit(): повертає True, якщо всі символи рядка - цифри
#
# print(text.isdigit())
#
# # isnumeric(): повертає True, якщо рядок є числом
#
# print(text.isnumeric())
#
# # startswith(str): повертає True, якщо рядок починається з підрядка str
#
# print(text.startswith("helLo"))
#
# # endswith(str): повертає True, якщо рядок закінчується на підрядок str
#
# print(text.endswith("D"))
#
# # lower(): перекладає рядок у нижній регістр
#
# print(text.lower())
#
# # upper(): перекладає рядок у верхній регістр
#
# print(text.upper())
#
# # title(): початкові символи всіх слів у рядку перекладаються у верхній регістр
#
# print(text.title())
#
# # capitalize(): перекладає у верхній регістр першу літеру тільки першого слова рядка
#
# print(text.capitalize())
#
# fio = input("Enter fio: ").title()
# print(fio)
#
# lstrip(): видаляє початкові пробіли з рядка
# text = "helLo woRlD"
# print(text)
# print(text.lstrip())
#
# # rstrip(): видаляє кінцеві пробіли з рядка
# print(text)
# print(text.rstrip())
#
# # strip(): видаляє початкові та кінцеві пробіли з рядка
# print(text)
# print(text.strip())
#
# ljust(width): якщо довжина рядка менша за параметр width, то праворуч від рядка додаються пробіли,
# щоб доповнити значення width, а сам рядок вирівнюється по лівому краю
# text = "hello world"
# print(text)
# print(text.ljust(20))
#
# # rjust(width): якщо довжина рядка менша за параметр width, то зліва від рядка додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється праворуч
# text = "hello world"
# print(text)
# print(text.rjust(20))
#
# # center(width): якщо довжина рядка менша за параметр width, то ліворуч і праворуч від рядка рівномірно додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється по центру
# text = "hello world"
# print(text)
# print(text.center(20))

# find(str[, start [, end]): повертає індекс підрядка у рядку. Якщо підрядок не знайдено, повертається число -1
text = "hello world"
# print(text.find("hello"))  # 0
# print(text.find("l"))  # 2
# print(text.rfind("l"))  # 9
#
# first_found_index = text.find("l")
# print(text.find("l", first_found_index + 1))
#
# print(text.find("p"))  # -1

# # v1
# for i in range(len(text)):
#     if text[i] == "l":
#         print(i)
#
# # v2
# index = 0
#
# for letter in text:
#     if letter == "l":
#         print(index)
#     index += 1

#

# replace(old, new[, num]): замінює в рядку один підрядок на інший
# text = "hello world hello"
# print(text)
#
# text = text.replace("hello", "goodbye", 1)
# print(text)

###

