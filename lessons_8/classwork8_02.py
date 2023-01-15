"""Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет атрибут имени у объекта. Создать один объект
 класса. Вывести имя. Вызвать метод change_name. Вывести имя. """
class Dog:
    height = None
    weight = None  #атрибуты
    name = None
    age = None

    def __init__(self,height, weight, name, age):
        self.height,self.weight, self.name, self.age= height, weight, name, age

    def jump(self):
        print (f"{self.name} is jumping")

    def run(self):
        print(f"{self.name} is running")

    def bark(self):
        print(f"{self.name} is barking")

    def change_name(self,name):
        self.name=name


if __name__=="__main__":
    dog = Dog (100,50, "My dog",10)

    dog.jump()
    dog.change_name("New Name")  #меняем имя на new name
    dog.jump()

