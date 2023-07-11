# Description

Object to iterate through different variables, instead of nesting a number of loops, one can run through all of them in a single loop.

The advantage is that instead of writing this:

```python
features = [6,3,56]
epochs = [50,23]
monitors = [10,412,14]

for feature in features:
    for epoch in epochs:
        for monitor in monitors:
            print(f"{feature,epoch,monitor}") 
```

One gets an iterator that runs through all the possible conbinations:

```python
iterator = VariableIterator(Features = features,Epochs = epochs,Monitor = monitors)
for feature,epoch,monitor in iterator:
    print(f"{feature,epoch,monitor}") 
```

# Usage

Just download the `variable_iterator.py` module. Then simply import:
```python
from variable_iterator import VariableIterator
```
# Extra features

The variables names are accessible with the attribute `variables_names`. This may be helpful if one needs the variables to be in a dictionary:
```python
iterator = VariableIterator(Features = features,Epochs = epochs,Monitor = monitors)
for variables in iterator:
    variable_dict = dict(zip(iterator.variables_names,variables))
    print(variable_dict) 
```

Alternatively, one can directly obtain the variables as dictionary by running the method `as_dict` after initializing the iterator:
```python
iterator = VariableIterator(Features = features,Epochs = epochs,Monitor = monitors).as_dict()
for variable_dict in iterator:
    print(variable_dict) 
```