import lasagne

nonlinearity_map = {
    'sigmoid': lasagne.nonlinearities.sigmoid,
    'tanh': lasagne.nonlinearities.tanh,
    'softmax': lasagne.nonlinearities.softmax,
    'relu': lasagne.nonlinearities.rectify,
}

update_map = {
    'adagrad': lasagne.updates.adagrad,
}

loss_map = {
    'multiclass_hinge_loss': lasagne.objectives.multiclass_hinge_loss,
}

class Params(object):
    """Simple container class for parameters."""
    def __init__(self, *initial_data, **kwargs):
        self.keys = set()
        for dictionary in initial_data:
            for key in dictionary:
                self.keys.add(key)
                setattr(self, key, dictionary[key])
        for key in kwargs:
            self.keys.add(key)
            setattr(self, key, kwargs[key])

    def __str__(self):
        out = ""
        for key in self.keys:
            out += "%s: %s\n" % (key, getattr(self, key))
        return out

    def set(self, instance, value):
        self.keys.add(instance)
        setattr(self, instance, value)