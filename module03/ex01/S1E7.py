from S1E9 import Character

class Baratheon(Character):
    """Representing the Barathon family."""
    def __init__(self, first_name, is_alive=True):
        """Initialize Baratheon character with first name and alive status."""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        return f"Vector: ('{self.first_name}, {self.eyes}, {self.hairs}"
   
    def __repr__(self):
        return self.__str__()
    
    def die(self):
        self.is_alive = False

class Lannister(Character):
    """Сlass Lannister inherited from Character."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'
    def __str__(self):
        return f"Vector: ('{self.family_name}, {self.eyes}, {self.hairs}"
    def __repr__(self):
        return self.__str__()
    def die(self):
        """Baratheon method die."""
        self.is_alive = False
    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)