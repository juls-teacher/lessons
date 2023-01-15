from lessons_8.library.animal import Animal

class Cat(Animal):

    def meow(self):
        print(f"{self.name} is meowing")


if __name__=="__main__":


    cat=Cat(100,50,"My Cat",10)
    cat.meow()