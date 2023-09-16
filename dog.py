class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.\n")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.\n")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, activity_level):
        super().__init__(name, age, coat_color)
        self.activity_level = activity_level

    def special_skill(self):
        print(f"{self.name} can jump really high!\n")

    def barking(self):
        print(f"{self.name} barks loudly when excited.\n")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, wrinkles):
        super().__init__(name, age, coat_color)
        self.wrinkles = wrinkles

    def special_skill(self):
        print(f"{self.name} has a strong grip.\n")

    def snoring(self):
        print(f"{self.name} snores loudly while sleeping.\n")


# Create instances of Dog subclasses
jack = JackRussellTerrier("Jack", 3, "white and brown", "high")
bully = Bulldog("Bully", 5, "gray", "wrinkled")

# Call methods on the objects
jack.description()
jack.get_info()
jack.special_skill()
jack.barking()

bully.description()
bully.get_info()
bully.special_skill()
bully.snoring()
