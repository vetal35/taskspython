1.# Подсчитать сумму цифр в вещественном числе

#def sum_of_digits(num):
   # sum = 0
 #   while num > 0:
 #       sum += num % 10
      #  num //= 10
   # return sum

#print(sum_of_digits(1522)) 
#второй способ

float_num = input('input float number: ')
print(type(float_num))
sum = 0
for i in float_num:
if i != '.':
sum += int(i)
print(sum)