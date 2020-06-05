MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, name, birthday):
        
        values = self.values()
        
        day_month = [(d_birthday.month, d_birthday.day) for d_birthday in self.values()]
            
        if (birthday.month, birthday.day) in day_month:
                
            global MSG
            name_msg = MSG.format(name)
            print(name_msg)
        
        super().__setitem__(name, birthday)
            
            
