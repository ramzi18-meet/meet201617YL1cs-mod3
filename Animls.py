class Animal:
    def __init__(self, animal_name, animal_sound, animal_colour):
        self.name=animal_name
        self.sound=animal_sound
        self.colour=animal_colour
cat=Animal('Rexy', 'Meow' , 'White')
dog=Animal('Jack', 'Woof' , 'Brown')

print(cat.name)
print(dog.colour)
