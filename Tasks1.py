def perimeter(a):
    a = float(a)
    return f'Периметр квадрата равен: {4 * a}'

def square(a):
    a = float(a)
    return f'Площадь квадрата равна: {a ** 2}'

def rectangle(a, b):
    a, b = float(a), float(b)
    return f'Площадь прямоугольника равна: {a * b}, периметр равен: {2 * (a + b)}'

def length(d):
    d = float(d)
    p = 3.14
    return f'Длина окружности равно: {p * d}'

def cube(a):
    a = float(a)
    return f'Объем куба равен: {a ** 3}, площадь поверхности равна: {6 * (a ** 2)}'

def paralleliped(a, b , c):
    a, b , c = float(a), float(b), float(c)
    return f'Объем параллелепипеда равен: {a * b * c}, площадь его поверхности равна: {2 * (a * b + b * c + a * c)}'

def circle(r):
    r = float(r)
    p = 3.14
    return f'Длина окружности равна: {2 * p * r}, площадь круга равна: {p * (r ** 2)}'

def arithmetic(a, b):
    a, b = float(a), float(b)
    return f'Среднее арифметическое чисел равно: {(a + b) / 2}'

def geometric(a, b):
    a, b = float(a), float(b)
    if a >= 0 and b >= 0:
        return f'Среднее геометрическое чисел равно: {(a * b) ** 0.5}'
    else:
        return 'Числа должны быть неотрицательными'
def numbers(a, b):
    a, b = float(a), float(b)
    if a != 0 and b != 0:
        a, b = a ** 2, b ** 2
        return f'Сумма квадратов чисел равна: {a + b}, разность равна: {a - b}, произведение равно: {a * b}, частное равно: {a / b}'
    else:
        return 'Числа не должны быть равны 0'
print(numbers(2,0))