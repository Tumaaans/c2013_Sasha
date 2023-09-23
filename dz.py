import random


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100

    def make_sound(self):
        pass

    def eat(self, food):
        if self.energy < 100:
            print(f"{self.name} їсть {food}.")
            self.energy += random.randint(5, 20)
            if self.energy > 100:
                self.energy = 100
        else:
            print(f"{self.name} не голодний.")

    def sleep(self):
        print(f"{self.name} спить.")
        self.energy += random.randint(10, 30)
        if self.energy > 100:
            self.energy = 100

    def play(self):
        if self.energy >= 30:
            print(f"{self.name} грається.")
            self.energy -= random.randint(10, 20)
        else:
            print(f"{self.name} занадто втомлений для гри.")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Кіт")

    def make_sound(self):
        print(f"{self.name} мурчить.")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Собака")

    def make_sound(self):
        print(f"{self.name} гавкає.")


# Приклад використання класу:

my_cat = Cat("Мурка")
my_dog = Dog("Рекс")

for _ in range(5):
    my_cat.make_sound()
    my_cat.play()
    my_cat.eat("печиво")
    my_cat.sleep()
    print(f"Енергія {my_cat.name}: {my_cat.energy}")

for _ in range(5):
    my_dog.make_sound()
    my_dog.play()
    my_dog.eat("кістка")
    my_dog.sleep()
    print(f"Енергія {my_dog.name}: {my_dog.energy}")
