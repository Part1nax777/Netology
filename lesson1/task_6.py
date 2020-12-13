import math

print('Введите тип фигуры:')
type_figure = input()
type_figure = type_figure.lower()

if type_figure == 'круг':
	print('Введите радиус круга:')
	radius = int(input())
	circle_area = math.pi * (radius ** 2)
	print('Результат:')
	print('Площадь круга:', round(circle_area, 2))
elif type_figure == 'треугольник':
	print('Введите длину стороны А:')
	side_A = int(input())
	print('Введите длину стороны B:')
	side_B = int(input())
	print('Введите длину стороны С:')
	side_C = int(input())
	semi_perimetr = (side_A + side_B + side_C) / 2
	triangle_area = math.sqrt(semi_perimetr * (semi_perimetr - side_A) * (semi_perimetr - side_B) * (semi_perimetr - side_C))
	print('Результат:')
	print('Площадь треугольника:', round(triangle_area, 2))
elif type_figure == 'прямоугольник':
	print('Введите длину прямоугольника:')
	length = int(input())
	print('Введите ширину прямоугольника:')
	width = int(input())
	rectangle_area = length * width
	print('Результат:')
	print('Площадь прямоугольника:', round(rectangle_area, 2))
else:
	print('Ошибка при выборе типа фигуры')
