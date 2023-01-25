"""Создать генератор и/или итератор простой геометрической прогрессии."""
"""
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
print(next(a))"""

import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def my_generator(power: int, limit: int):
    for current in range(1, limit + 1):
        yield current * power


if __name__ == "__main__":
    my_geo = my_generator(power=2, limit=5)
    logger.info(next(my_geo))
    logger.info(next(my_geo))
    logger.info(next(my_geo))
    for item in my_geo:
        logger.info(item)




