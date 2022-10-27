# Подсчитать сумма чисел в вещественном числе.

from random import uniform

n = round(uniform(1, 100), 3)

def sum_digit(n):
    return sum(map(int, list(str(n).replace('.',''))))

print(f"Дано вещественное число {n}")
print(sum_digit(n))