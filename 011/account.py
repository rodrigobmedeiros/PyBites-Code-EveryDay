class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
    def __len__(self):
        
        return len(self._transactions)

    def __gt__(self, other):
        
        return self.balance > other.balance
        
    def __ge__(self, other):
        
        return self.balance >= other.balance
        
    def __lt__(self, other):
        
        return self.balance < other.balance
        
    def __le__(self, other):
        
        return self.balance <= other.balance
        
    def __eq__(self, other):
        
        return self.balance == other.balance
        
    def __getitem__(self, n):
        
        return self._transactions[n]
         
    def __list__(self):
        
        return self._transactions
    
    def __add__(self, value):
        
        if not isinstance(value, int):
            
            raise ValueError('Please add an integer')
            
        self._transactions.append(value)
        return self.balance
    
    def __sub__(self, value):
        
        if not isinstance(value, int):
            
            raise ValueError('Please subtract an integer')
        
        self._transactions.append(-1 * value)
        return self.balance
        
    def __str__(self):
        
        return f'{self.name} account - balance: {self.balance}'