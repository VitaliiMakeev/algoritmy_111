"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!

Решите через рекурсию. В задании нельзя применять циклы.
"""


def sum_numbers(num, res=0):
    if num == 0:
        return res
    else:
        res += num
        num -= 1
        return sum_numbers(num, res)


def check_num(n):
    num = sum_numbers(n)
    if num == n * (n + 1) / 2:
        return True
    else:
        return False


print(check_num(6))