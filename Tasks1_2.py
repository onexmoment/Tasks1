def distance(l):
    l = int(l)
    return f'Расстояние полных {l // 100} м'

def weight(m):
    m = int(m)
    return f'Масса полных {m // 1000} т'

def file(b):
    b = int(b)
    return f'Файл занимает полных {b // 1024} кб'

def pieces(a, b):
    a, b = int(a), int(b)
    return f'{a // b} - количество отрезков B в A'

def pieces2(a , b):
    a, b = int(a), int(b)
    return f'{a % b} - длина незанятой части отрезка A'

def left_right(a):
    a = int(a)
    return f'{a // 10} - левая цифра, {a % 10} - правая цифра'

def number_sum(a):
    a = int(a)
    left = a // 10
    right = a % 10
    return f'Сумма цифр равна {left + right}, произведение равно {left * right}'

def number_trans(a):
    a = int(a)
    left = a // 10
    right = a % 10
    return f'{right}{left} - после перестановки цифр'

def three_digit(a):
    a = int(a)
    return f'Первая цифра {a // 100}'

def three_digit2(a):
    a = int(a)
    return f'Последняя цифра {a % 10}, по середине цифра {a % 100 // 10}'