def countdown():
    """Write a generator that counts from 100 to 1"""
    
    for number in reversed(range(1, 101)):
        
        yield number