# class Warrior:

#     def __init__(self, name, hp, attack_points, magic_points, status_effect):
#         self.name = name
#         self.hp = hp
#         self.attack_points = attack_points
#         self.magic_points = magic_points 
#         self.status_effect = status_effect

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, name):
#         if type(name) == str:
#             self._name = name
#         else:
#             raise Exception("Warrior name must be a string")
        
#     @property
#     def hp(self):
#         return self._hp
    
#     @hp.setter
#     def hp(self, hp):
#         if type(hp) == int:
#             self._hp = hp
#         else:
#             raise Exception("HP must be an Integer")
        
#     @property
#     def attack_points(self):
#         return self._attack_points
    
#     @attack_points.setter
#     def attack_points(self, attack_points):
#         if type(attack_points) == int:
#             self._attack_points = attack_points
#         else:
#             raise Exception("Attack Points must be an Integer")
        
#     @property
#     def magic_points(self):
#         return self._magic_points
    
#     @magic_points.setter
#     def magic_points(self, magic_points):
#         if type(magic_points) == int:
#             self._magic_points = magic_points
#         else:
#             raise Exception("Magic point was not and Integer")


#     @property
#     def status_effect(self):
#         return self._status_effect
    
#     @status_effect.setter
#     def status_effect(self, status_effect):
#         if type(status_effect) == int:
#             self._status_effect = status_effect
#         else:
#             raise Exception("Status points was not an Integer")

