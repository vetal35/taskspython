numbers_type = None
num1 = None
num2 = None
operand = None
data = ''
operands = [['+', '-', '*', '/'], [1, 2, 3, 4]]
while True:
      print('с какими числами будем работать?'
            '\n 1 - рациональные \n 2 - комплексные \n (введите цифру)')
      try:
            numbers_type = int(input())
            if numbers_type == 1 or numbers_type == 2:
                  break
            else:
                  print('введено неправильное значение, ещё раз:')
      except:
            print('введены некорректные данные, попробуйте ещё раз')
while True:
      if numbers_type == 1:
            try:
                  import fractions
                  num1 = fractions.Fraction(int(input('введите числитель 1-го числа: ')),
                                            int(input('введите знаменатель 1-го числа: ')))
                  operand = operands[1][operands[0].index(input('выберите действие (+, -, *, /): '))]
                  num2 = fractions.Fraction(int(input('введите числитель 2-го числа: ')),
                                            int(input('введите знаменатель 2-го числа: ')))
                  import calc_rational as rat
                  print(rat.rational(num1, num2, operand))
                  data = str(num1)+' '+operands[0][operands[1].index(operand)]+' '+str(num2)\
                         +' = '+str(rat.rational(num1, num2, operand))
                  break
            except:
                  print('введены некорректные данные, попробуйте ещё раз!')
      else:
            try:
                  num1 = complex(input('введите 1-е число в формате 1+2j: '))
                  operand = operands[1][operands[0].index(input('выберите действие (+, -, *, /): '))]
                  num2 = complex(input('введите 2-е число в формате 1+2j: '))
                  import calc_complex as comp
                  print(comp.complex(num1, num2, operand))
                  data = str(num1)+' '+operands[0][operands[1].index(operand)]+' '+str(num2)\
                         +' = '+str(comp.complex(num1, num2, operand))
                  break
            except:
                  print('введены некорректные данные, попробуйте ещё раз!')
import logger as lg
lg.data_log(data, 2)