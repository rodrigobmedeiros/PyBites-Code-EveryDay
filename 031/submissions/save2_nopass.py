import numpy as np

class Matrix(object):

    def __init__(self, values):
        self.values = values
        self.col = len(values[0])
        self.row = len(values)
        
    def __repr__(self):
        return f'<Matrix values="{self.values}">'
        
    def __matmul__(self, other):
        
        arr_self_values = np.array(self.values)
        arr_other_values = np.array(other.values)
        arr_results = np.zeros((self.row, self.col))
        
        for i in range(self.row):
            
            for j in range(self.col):
                
                arr_results[i, j] = sum(arr_self_values[i, :] * arr_other_values[:, j])
                
        
        return list(arr_results)
        
    def __rmatmul__(self, other):
        
        arr_self_values = np.array(self.values)
        arr_other_values = np.array(other.values)
        arr_results = np.zeros((self.row, self.col))
        
        for i in range(self.row):
            
            for j in range(self.col):
                
                arr_results[i, j] = sum(arr_other_values[i, :] * arr_self_values[:, j])
    
        return list(arr_results)
        
    def __imatmul__(self, other):
        
        arr_self_values = np.array(self.values)
        arr_other_values = np.array(other.values)
        arr_results = np.zeros((self.row, self.col))
        
        for i in range(self.row):
            
            for j in range(self.col):
                
                arr_results[i, j] = sum(arr_other_values[i, :] * arr_self_values[:, j])
                
        
        sel.values = list(arr_results)