# Description

Object to iterate through different variables, instead of nesting a number of loops, you can run through all of them in a single loop

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

You get an iterator that runs through all the possible conbinations:

```python
iterator = VariableIterator(Features = features,Epochs = epochs,Monitor = monitors)
    for feature,epoch,monitor in iterator:
        print(f"{feature,epoch,monitor}") 
```