"""Создать генератор и/или итератор простой геометрической прогрессии."""

def progress():
    n = 7 # число элементов прогрессии
    q = 3 # знаменатель
    b_first = 3 # первый элемент прогрессии
    b_next = b_first
    for i in range(1,n):
        b_curn = b_next * q
        yield b_curn
        b_next = b_curn


a = progress()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))



