#.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
k = int(input('Please input integer: ')) 
k1 = 0
k2 = 1
if k <= 0:
    k = input('Input integer > 0: ')
elif k == 1:
    print(k1)
elif k == 2:
    print(k2)
else:
    print(0, 1, end=' ')
    for i in range(2, k):
        k1, k2 = k2, k1 + k2
        print(k2, end=' ')
