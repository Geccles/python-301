class Animal:
    # fur_color = "orange"

    animal_type = "unknown"

    # this is a dunder
    def __init__(self, fur_color):
        print(f"My fur color is {fur_color}")
        self.fur_color = fur_color

    def sound(self):
        print("rawwr")

    def eat(self):
        print("I am eating...")
    # implement your own function
    def chase(self):
        raise NotImplementedError

# Extend

class Tiger(Animal):
    pass
class HouseCat(Animal):

    def __init__(self, fur_color):
        super().__init__(fur_color)
        print("Fur color was saved to the class Object")
        self.animal_type = "house cat"
        print(self.animal_type)

    def sound(self):
        print("meow")

    def chase(self):
        print("runnnn")

    def eat(self):
        super().eat()
        print("I am eating salmon")

house_cat = HouseCat("Grey")
print(type(house_cat))
house_cat.sound()
house_cat.chase()
house_cat.eat()
print(house_cat.fur_color)

tiger = Tiger("orange")
print(type(tiger))
tiger.sound()
print(tiger.fur_color)
    
# init
cat = HouseCat("Black")
print(cat.fur_color)
