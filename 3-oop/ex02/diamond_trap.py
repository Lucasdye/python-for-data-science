from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    
    def __init__(self, first_name, is_alive=True):
       super().__init__(first_name)
       self._eyes = self.eyes
       self._hairs = self.hairs
    
    # eyes att is now a Property Object that
    #    1) allows using methods as attributes
    #    2) allows to create a setter @x.setter
    #    3) allows to create a getter @x.getter
    #    4) return something based on another attribute
    @property
    def eyes(self):
        return self._eyes

    # WRAPPER /!\
    def set_eyes(self, color):
        self.eyes = color
    
    @eyes.setter
    def eyes(self, color):
        self._eyes = color
    
    # WRAPPER /!\
    def get_eyes(self):
        return self.eyes
    
    @eyes.getter
    def eyes(self):
        return self.eyes
    

# tester
Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
# Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
# print(Joffrey.get_hairs())
# print(Joffrey.__dict__)