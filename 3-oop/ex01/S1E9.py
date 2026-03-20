from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract class for characters"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
    
    @abstractmethod
    def die(self, is_alive):
        self.is_alive = False

class Stark(Character):
    """Representing Stark family"""
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

