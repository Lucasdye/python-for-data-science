from S1E9 import Character

class Baratheon(Character):
    """Representing of the Baratheon family"""
    family_name = "Baratheon"
    eyes = "brown"
    hairs = "dark"

    def __init__(self, first_name: str, is_alive=True):
        """Constructor

        Args:
            first_name (str): name of the character
            is_alive (bool, optional): health state. Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Sets 'is_alive' to False."""
        self.is_alive = False
    
    def __repr__(self):
        """String representation of the object"""
        return f"({self.family_name}, {self.eyes}, {self.hairs})"
    
    def __str__(self):
        """Printed string representation of the object"""
        return f"({self.family_name}, {self.eyes}, {self.hairs})"
        


class Lannister(Character):
    """Representing of the Lannister family"""
    family_name = "Lannister"
    eyes = "blue"
    hairs = "light"


    def __init__(self, first_name: str, is_alive=True):
        """Constructor

        Args:
            first_name (str): name of the character
            is_alive (bool, optional): health state. Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Sets 'is_alive' to False."""
        self.is_alive = False
    
    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool=True):
        """Factory method"""
        return cls(first_name, is_alive)
    
    def __repr__(self):
        """String representation of the object"""
        return f"({self.family_name}, {self.eyes}, {self.hairs})"
    
    def __str__(self):
        """Printed string representation of the object"""
        return f"({self.family_name}, {self.eyes}, {self.hairs})"
        


