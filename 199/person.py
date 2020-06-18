# see __mro__ output in Bite description

class Person(object):
    
    def __init__(self):
        
        pass
    
    def __str__(self):
        
        text2print = 'I am a person'
        return text2print
        
class Father(Person):
    
    def __str__(self):
        
        text2print = super().__str__() + ' and cool daddy'
        return text2print
    
class Mother(Person):
    
    def __str__(self):
        
        text2print = super().__str__() + ' and awesome mom'
        return text2print
    
class Child(Father, Mother):
    
    def __str__(self):
        
        text2print = 'I am the coolest kid'
        return text2print