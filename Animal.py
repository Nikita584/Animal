class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'Любимая еда {food}')

    def sound(self, sound):
        print(f'Звук который он любит издавать {sound}')
class Lion(Animal):
    pass

class Cat(Animal):
    pass

Lion1 = Lion('Лев')
Lion1.eat('мясо')
print(Lion1.name)
Lion1.sound('рык')


Cat1 = Cat('Кошка')
Cat1.eat('кошачий корм')
print(Cat1.name)
Cat1.sound('миау')






