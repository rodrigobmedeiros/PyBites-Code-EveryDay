class IntList(list):
    
    def __init__(self, value):
        
        super().__init__(value)
        self.value = self.check_input_values(value)
        self.mean = 0
        self.median = 0
        self.calculate_mean()
        self.calculate_median()
    
    def check_input_values(self, value):
        
        if isinstance(value, list):

            try:

                value = [int(x) for x in value]
            
            except:

                raise TypeError()

        else:

            try:

                value = int(value)

            except:

                raise TypeError()
                
        return value
    
    def calculate_mean(self):

        self.mean = sum(self.value) / len(self.value)
        return self.mean

    def calculate_median(self):

        length = len(self.value)

        is_pair = length % 2 == 0
        
        sorted_value = sorted(self.value)

        if is_pair:

            n_1 = length // 2 - 1
            n_2 = n_1 + 1
            self.median = (sorted_value[n_1] + sorted_value[n_2]) / 2

        else:

            n = length // 2
            self.median = sorted_value[n]      

    def __add__(self, other):

        other = self.check_input_values(other)

        new_value = list(self.value)

        [new_value.append(x) for x in other]

        self.calculate_mean()
        self.calculate_median()

        return IntList(new_value)

    def __iadd__(self, other):

        other = self.check_input_values(other)

        [self.value.append(x) for x in other]

        self.calculate_mean()
        self.calculate_median()
        return IntList(self.value)

    def append(self, other):
        
        other = self.check_input_values(other)
        self.value.append(other)
        self.calculate_mean()
        self.calculate_median()

teste = IntList([1, 2, 3])
print(teste)
teste.append(7)

print(teste.value)
print(teste.mean)
print(teste.median)