from dataclasses import dataclass

@dataclass
class Bite(object):
    
    number: int
    title: str
    level: str = 'Beginner'
    
    def __post_init__(self):
        
        self.title = self.title.capitalize()
        
    def __eq__(self, other):
        
        return self.number == other.number
    
    def __gt__(self, other):
        
        return self.number > other.number
    
    def __ge__(self, other):
        
        return self.number >= other.number
    
    def __lt__(self, other):
        
        return self.number < other.number
    
    def __le__(self, other):
        
        return self.number <= other.number