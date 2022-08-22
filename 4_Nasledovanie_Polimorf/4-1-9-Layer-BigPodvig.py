class Layer:
    def __init__(self, next_layer=None, name='Input'):
        self.next_layer = next_layer
        self.name = 'Layer'

    def __call__(self, *args, **kwargs):
        self.next_layer = Layer()
        return self.next_layer


class Input(Layer):
    def __init__(self, inputs: int):
        self.inputs = inputs
        self.name = 'Input'
        super().__init__(name='Input')


class Dense(Layer):
    def __init__(self, inputs: int, outputs: int, activation: str):
        super(Dense, self).__init__(name='Dense')
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation

class NetworkIterator:
    def __init__(self, obj):
        self.obj=obj

    def __iter__(self):
        flag=True
        if flag:
            flag=False
            yield self.obj.next_layer
        yield self.obj

network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))