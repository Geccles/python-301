# class MyFirstClass:
#     pass

# myClass = MyFirstClass()


class Animal:
    type = "mammal"
    sounds = ["roar", "meow", "prrr"]
    color = {
        "fur": "yellow",
        "eyes": "brown",
        "paws": "black",
        "nose": "pink"
    }

    # self is Animal class and has access to all properties
    def a_method_function(self):
        print(self.color)
    @property
    def get_animal_sound(self):
        return self.sounds[2]
    def add_sound(self, soundName):
        self.sounds.append(soundName)
        return self.sounds

this_animal = Animal()
this_animal.a_method_function()
animal_sound = this_animal.get_animal_sound
print(f"The animal sound has {animal_sound}")

this_animal.add_sound("grrr")
print(this_animal.sounds)
