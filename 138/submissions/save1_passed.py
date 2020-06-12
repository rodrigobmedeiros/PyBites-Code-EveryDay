class Animal:
    
    # First idea, create an instance counter.
    count_instances = 10000
    code_animals = []
    
    def __init__(self, name):
        
        self.name = name
        
        # Update counter.
        __class__.count_instances += 1
        
        # Define the code for actual instance
        self.code_instance = f'{__class__.count_instances}. {self.name.title()}'
        
        # Append actual code into complete codes list.
        __class__.code_animals.append(self.code_instance)
        
    def __str__(self):
        
        return self.code_instance

    @classmethod
    def zoo(cls):
        
        return cls.code_animals