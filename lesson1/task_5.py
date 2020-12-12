print('Введите номер билета:')
number = input()

sum_first_numbers = int(number[0]) + int(number[1]) + int(number[2])
sum_last_numebers = int(number[3]) + int(number[4]) + int(number[5])

print('number = {}'.format(number))
print('Результат:')
if sum_first_numbers == sum_last_numebers:
	print('Счастливый билет')
else:
	print('Несчастливый билет')
