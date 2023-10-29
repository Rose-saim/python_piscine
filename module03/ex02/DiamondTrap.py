from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    def set_eyes(self, eyes):
        self.eyes = eyes
    
    def set_hairs(self, hairs):
        self.hairs = hairs
        
    def get_eyes(self):
        """get King eyes."""
        return self.eyes

    def get_hairs(self):
        """get King hairs."""
        return self.hairs