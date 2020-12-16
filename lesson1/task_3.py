date = int(input('Введите день: '))
month = input('Введите месяц: ')
month = month.lower()

if (month == "март" and date >= 21) or (month == "апрель" and date <= 20):
	print('Ваш знак зодиака Овен')
elif (month == "апрель" and date >= 21) or (month == "май" and date <= 21):
	print('Ваш знак зодиака Телец')
elif (month == "май" and date >= 22) or (month == "июнь" and date <= 21):
	print('Ваш знак зодиака Близнецы')
elif (month == "июнь" and date >= 22) or (month == "июль" and date <= 22):
	print('Ваш знак зодиака Рак')
elif (month == "июль" and date >= 23) or (month == "август" and date <= 21):
	print('Ваш знак зодиака Лев')
elif (month == "август" and date >= 22) or (month == "сентябрь" and date <= 23):
	print('Ваш знак зодиака Дева')
elif (month == "сентябрь" and date >= 24) or (month == "октябрь" and date <= 23):
	print('Ваш знак зодиака Весы')
elif (month == "октябрь" and date >= 24) or (month == "ноябрь" and date <= 22):
	print('Ваш знак зодиака Скорпион')
elif (month == "ноябрь" and date >= 23) or (month == "декабрь" and date <= 22):
	print('Ваш знак зодиака Стрелец')
elif (month == "декабрь" and date >= 23) or (month == "январь" and date <= 20):
	print('Ваш знак зодиака Козерог')
elif (month == "январь" and date >= 21) or (month == "февраль" and date <= 19):
	print('Ваш знак зодиака Водолей')
elif (month == "февраль" and date >= 20) or (month == "март" and date <= 20):
	print('Ваш знак зодиака Рыбы')
else:
	print('Проверьте вводимые данные!')
