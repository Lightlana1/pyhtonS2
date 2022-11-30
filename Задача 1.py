# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Вариант 1:
# num = float(input('Введите число: '))
# sum = 0
# if num >= 1:
#     while num > 0:
#             sum = sum + num % 10
#             num = num // 10
# if num < 1:
#     while num != int(num):
#         num *= 10
#         print(num)
#     while num > 0:
#         sum = sum + num % 10
#         num = num // 10
# print("Сумма цифр числа равна: ", sum)

#Вариант2
num = float(input('Введите число: '))
lst = [str(i) for i in str(num)]
lst.remove('.')
lst.remove('0')
print(lst)
summ = 0
num = list(map(int, lst))
print(num)
for i in range (len(num)):
    summ = summ + num[i]
print(summ)

