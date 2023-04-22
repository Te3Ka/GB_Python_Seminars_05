'''
Факториал через рекурсию
'''

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

_n = int(input('n = '))
print(factorial(_n))