print('Укажите ширину:')
width = int(input())
print('Укажите длину:')
length = int(input())
print('Укажите высоту:')
height = int(input())

if (width < 15) and (length < 15) and (height < 15):
	print('Коробка №1')
elif length > 200:
	print ('Упаковка для лыж')
elif (15 < width < 50) or (15 < length < 50) or (15 < height < 50):
	print('Коробка №2')
else:
	print('Коробка №3')
