def integer_params_decorated(func, vector_log):
    def wrapper(self, *args):
        vector_log.append(func.__name__)
        return func(self, *args)
    return wrapper

def class_log(vector_log):
    def wrapper(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, integer_params_decorated(v, vector_log))
        return cls
    return wrapper

vector_log = [] 


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value
