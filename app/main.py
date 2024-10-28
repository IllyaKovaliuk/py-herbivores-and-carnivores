class Animal:
    alive = []

    def __init__(self, name, health: int = 100, is_hidden: bool = False):
        self.name = name
        self.health = health
        self.is_hidden = is_hidden
        self.alive.append(self)


    def die(self):
        if self in Animal.alive:
            self.alive.remove(self)

    def __repr__(self):
        return f"Animal(name={self.name}, health={self.health}, hidden={self.is_hidden})"

    @classmethod
    def print_alive(cls):
        return "\n".join(str(animal) for animal in cls.alive)


class Herbivore(Animal):

    def hide(self) -> bool:
        self.is_hidden = not self.is_hidden
        return self.is_hidden


class Сarnivore(Animal):

    def bite(self, target):
            if not target.is_hidden:
                target.health -= 50
                if target.health <= 0:
                    target.health = 0
                    target.die()
            else:
                target.health = 100




rabbit = Herbivore("Rabbit")
print(rabbit)
lion = Сarnivore("Lion")
print(lion)


lion.bite(rabbit)
print(rabbit.health)
lion.bite(rabbit)
print(rabbit.health)
print(Animal.alive)