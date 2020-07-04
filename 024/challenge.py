from abc import ABC, abstractmethod


class Challenge(ABC):
    
    def __init__(self, number, title):
        
        self.number = number
        self.title = title
        
    
    @abstractmethod
    def verify(self):
        
        pass
    
    @property
    @abstractmethod
    def pretty_title(self):
        
        pass
        
        


class BlogChallenge(Challenge):
    
    def __init__(self, number, title, merged_prs):
        
        super().__init__(number, title)
        self.merged_prs = merged_prs
        
    def verify(self, value):
        
        return value in self.merged_prs
        
    @property
    def pretty_title(self):
        
        return f'PCC{self.number} - {self.title}'
        

class BiteChallenge(Challenge):
    
    def __init__(self, number, title, result):
        
        super().__init__(number, title)
        self.result = result
    
    def verify(self, text):
    
        return text == self.result
    
    @property   
    def pretty_title(self):
        
        return f'Bite {self.number}. {self.title}'