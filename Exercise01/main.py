'''
Последовательностью Фибоначчи называется последовательность чисел
a0, a1 , ..., an , ...,
где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
'''

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

_n = int(input('n = '))
print(fibonacci(_n))