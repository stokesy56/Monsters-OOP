from monster_class import *
# class Monster():
#     def __init__(self, name, eyes, fur, skills, cuteness):
#         self.name = name
#         self.eye_colour = eyes
#         self.fur = fur
#         self.skills = skills
#         self.cuteness = cuteness
monster1 = Monster('Jason',22, 'patchy and grey', ['fire breather','can fly', 'can juggle'],'not cute')
monster2 = Monster('Angelina',1,'thick and murky green',['climbs walls, great at taxes, can turn into goat'], 'not cute')
monster3 = Monster('Kevin',2,'wispy, long and black', ['fire breather','can turn into goat','stand-up comedy'],'very cute')

print(monster1.name)
print(monster1.breath_fire())
print(monster2.eat())
print(monster2.transfrom())
print(monster3.skills[1])
print(monster3.joke())