from decimal import Decimal

result_float = 0.1 + 0.2
print(result_float)

result_decimal = Decimal('0.1') + Decimal('0.2')
print(result_decimal)


from decimal import Decimal, getcontext

getcontext().prec = 4

value1 = Decimal('1.23456')
value2 = Decimal('7.89012')
result = value1 * value2

print('Результат:', result)