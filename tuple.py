#1
# t = tuple(range(1,43))
# a = t[2]
# b = t[-1]
# print(a,b)

#2
# t = []
# n = input("Введите число: ")
# for i in range(1,int(n)+1):
#     t.append(i)
# t2 = tuple(t)
# print(t2)

#3
# t = input("Введите текст: ")
# tup = tuple(t)
# print(tup)

#4
# day = input("Введите день: ")
# month = input("Введите месяц: ")
# year = input("Введите год: ")
# day2 = input("Введите день: ")
# month2 = input("Введите месяц: ")
# year2 = input("Введите год: ")
#
# date1 = (int(day),int(month),int(year))
# date2 = (int(day2),int(month2),int(year2))
#
# if date1 < date2:
#     print("Первый старше")
# elif date1 > date2:
#     print("Второй старше")
# elif date1 == date2:
#     print("Возраст одинаков")
# else: print("Введите корректные данные")

#задача 5
# number = int(input("Введите число населения: "))
# if number % 2 == 0:
#     n = number/2
#     print(n)
# else: n = number/2 + 0.5
# print(n)

#задача 6
# n = int(input("Введите ваш номер в вагоне: "))
# print((n + 3)//4)

#задача 7
#number = int(input("Введите кол-во минут: "))
#hours = number//60
#minutes = number%60
#print(f'{number} минут - это {hours} часov {minutes} минут')

#задача 8
# res = 1
# numbers = input("Введите числа через пробел: ").split(' ')
# for i in numbers:
#     if i == ' ':
#         continue
#     res *= int(i)
# print(res)

#задача 9
# res = 1
# res2 = []
# nums = input("Введите числа: ").split(' ')
# for i in nums:
#     suma = int(res) + int(i)
#     res = i
#     res2.append(suma)
# res2.remove(res2[0])
# print(res2)

#задача 10
#numbers = set(input('Введите числа: ').split(' '))
#maxnumber = max(numbers)
#numbers.remove(max(numbers))
#print(max(numbers))

#задача 11
# nums = input("Введите числа: ").split(' ')
# arr = 0
# nums2 = []
# for i in nums:
#     if i == '0':
#         arr += 1
#         continue
#     else:
#         nums2.append(i)
# for i in range(arr):
#     nums2.append('0')
# print(nums2)

#задача 12
nums = input('Введите числа: ').split(' ')
arr = []
for i in nums:
    if int(i)%2 == 0:
        arr.append(i)print(arr)