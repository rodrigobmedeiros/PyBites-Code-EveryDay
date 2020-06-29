class RecordScore():
    """Class to track a game's maximum score"""
    
    def __init__(self):
        
        self.max_score = None
        
    def __call__(self, score):
        
        if self.max_score == None or score > self.max_score:
            
            self.max_score = score
            return self.max_score
            
        else:
            
            return self.max_score
    
    