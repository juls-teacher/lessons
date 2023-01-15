"""Создать новый класс Cat, который имеет все те же атрибуты что и Dog, только заменить метод bark на meow."""

from lessons_8.library.dog import Dog
from lessons_8.library.cat import Cat


if __name__=="__main__":
    dog = Dog(100, 50, "My dog", 10)
    dog.bark()

    dog.change_name(name="New Name")  # меняем имя на new name
    dog.bark()

    cat=Cat(100,50,"My Cat",10)
    cat.meow()



