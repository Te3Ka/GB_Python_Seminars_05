'''
Напишите функцию,
которая принимает одно число и проверяет,
является ли оно простым
Напоминание: Простое число - это число,
которое имеет 2 делителя: 1 и n (само число)
Input: 5
Output: yes 
'''

def simple_number(n, i = 2):
    print(n, i)
    if i == n:
        return True
    elif i * i > n:
        return True
    elif n % i == 0:
        return False
    else:
        return simple_number(n, i + 1)

_n = int(input('n = '))
print(simple_number(_n, 2))