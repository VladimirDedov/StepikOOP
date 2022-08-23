class Layer:
    prev_layer = None

    def __init__(self, name='Layer'):
        self.name = name
        self.next_layer = None

    def __call__(self, *args, **kwargs):
        self.next_layer = args[0]
        return args[0]


class Input(Layer):
    def __init__(self, inputs: int):
        self.inputs = inputs
        super().__init__(name='Input')


class Dense(Layer):
    def __init__(self, inputs: int, outputs: int, activation: str):
        super(Dense, self).__init__(name='Dense')
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        while self.obj:
            yield self.obj
            self.obj = self.obj.next_layer


network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))
