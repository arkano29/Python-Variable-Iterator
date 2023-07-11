import numpy as np
class VariableIterator:
    def __init__(self,**variables_lists):
        self.variables_lists = variables_lists
        self.variables_names = list(variables_lists.keys())
        self.number_of_variables = len(variables_lists)
        self.lenghts = [len(variable_list) for variable_list in variables_lists.values()]
        self.number_of_outputs = np.prod(self.lenghts)
        self.indexes = [0 for _ in variables_lists]
        self.return_dict = False
        
    def as_dict(self):
        self.return_dict = True
        return self
        
    def __iter__(self):
        self.n = 0
        self.indexes = [0 for _ in self.variables_lists]
        return self
    
    def update_indexes(self):
        i = 0
        while self.indexes[i] == self.lenghts[i]-1 and (i<len(self.lenghts)-1):
            self.indexes[i] = 0
            i+=1
        self.indexes[i]+=1
    
    def __next__(self):
        if self.n >= self.number_of_outputs:
            self.n = 0
            self.indexes = [0 for _ in self.variables_lists]
            raise StopIteration
        variables = [self.variables_lists[self.variables_names[i]][self.indexes[i]] for i in range(self.number_of_variables)]
        self.n+=1
        self.update_indexes()
        if self.return_dict:
            return dict(zip(self.variables_names,variables))
        return tuple(variables)
      

def main():
    print("A single loop is used to run through 3 variables")
    
    features = [6,3,56]
    epochs = [50,23]
    monitors = [10,412,14]
    
    iterator = VariableIterator(Features = features,Epochs = epochs,Monitor = monitors)
    for feature,epoch,monitor in iterator:
        print(f"{feature,epoch,monitor}")  
    
    print("The same is obtained when nesting for loops in the same order")
    for feature in features:
        for epoch in epochs:
            for monitor in monitors:
                print(f"{feature,epoch,monitor}") 
                
    print("Print variables with their names")
    for variables in iterator:
        variable_dict = dict(zip(iterator.variables_names,variables))
        print(variable_dict) 
        
    print("Get dictionary directly")
    iterator = VariableIterator(Features = features,Epochs = epochs,Monitor = monitors).as_dict()
    for variable_dict in iterator:
        print(variable_dict) 
        
if __name__ == "__main__":
    main()
