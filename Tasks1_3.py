def positive(a):
    if a > 0:
        return True
    else:
        return False

def uneven(a):
    if a % 2 != 0:
        return True
    else:
        return False

def even(a):
    if a % 2 == 0:
        return True
    else:
        return False

def two_numbers(a, b):
    if a > 2 and b <= 3:
        return True
    else:
        return False

def three_numbers(a, b, c):
    if a < b < c:
        return True
    else:
        return False

def three_numbers_between(a, b, c):
    if a < b < c:
        return True
    else:
        return False

def two_uneven_numbers(a, b):
    if a % 2 != 0 and b % 2 != 0:
        return True
    else:
        return False

def any_of_two_uneven(a ,b):
    if a % 2 != 0 or b % 2 != 0:
        return True
    else:
        return False
def one_of_two_uneven_numbers(a, b):
    if a % 2 != 0 and b % 2 == 0:
        return True
    elif a % 2 == 0 and b % 2 != 0:
        return True
    else:
        return False
