import numpy as np
class VariableIterator:
    def __init__(self,**parameters_lists):
        self.parameters_lists = parameters_lists
        self.parameters_names = list(parameters_lists.keys())
        self.number_of_parameters = len(parameters_lists)
        self.lenghts = [len(parameter_list) for parameter_list in parameters_lists.values()]
        self.number_of_outputs = np.prod(self.lenghts)
        self.indexes = [0 for _ in parameters_lists]
        
    def __iter__(self):
        self.n = 0
        self.indexes = [0 for _ in self.parameters_lists]
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
            self.indexes = [0 for _ in self.parameters_lists]
            raise StopIteration
        parameters = [self.parameters_lists[self.parameters_names[i]][self.indexes[i]] for i in range(self.number_of_parameters)]
        self.n+=1
        self.update_indexes()
        return tuple(parameters)
      

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
        
if __name__ == "__main__":
    main()
