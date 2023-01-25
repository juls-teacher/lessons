"""Пользователь вводит два числа N и M, рассчитать последовательность  N + NN + NNN + ... + NxM."""
#n = int(input ("введите значение n: "))
#m = int(input ("введите значение m : "))
#g=(sum(n**m for m in range(1, m+1)))
#print(g)
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


class SymbolsIterator:
    def __init__(self, symbol: str, count: int):
        self.symbol = symbol
        self.current_value = symbol
        self.count = count

    def __next__(self) -> str:
        previous_value = self.current_value
        if len(self.current_value) <= self.count:
            self.current_value += self.symbol
            return previous_value
        else:
            raise StopIteration

    def __iter__(self):
        self.current_value = self.symbol
        return self


if __name__ == "__main__":
    my_sym = SymbolsIterator(symbol="N", count=5)
    for item in my_sym:
        logger.info(item)