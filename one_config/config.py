import yaml

__all__ = ['CONFIG']


class CONFIG:
    """
    The CONFIG object is an object whose attributes are the config params. In this way it
    acts like a typical `config.py` object. Going a step further, all nested parameters are
    represented as AttributeDicts, so they can be accessed with `CONFIG.my.nested.attr` rather
    than CONFIG.my['nested']['attr'].

    The CONFIG object must be constructed with the `construct_config()` class method once (and only
    once, at the beginning of the program. It is parametrized by a yaml file whose path is specified
    in the constructor method.

    Example:
        First, construct the config at the entry point of the program:
        >>> # run.py
        >>> from one_config import CONFIG
        >>> CONFIG.construct_config('path/to/prod_config.yaml')
        Then use it from any module in your codebase:
        >>> # my_module.py
        >>> from one_config import CONFIG
        >>> param1 = CONFIG.my.favorite.parameter
    """
    _is_constructed = False

    @classmethod
    def construct_config(cls, path):
        if cls._is_constructed:
            raise RuntimeError('This config object has already been constructed')
        with open(path, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        for key, value in data.items():
            if isinstance(value, dict):
                value = AttributeDict(value)
            setattr(cls, key, value)


class AttributeDict(dict):
    def __init__(self, dict_ = None):
        super().__init__(self)
        for key, value in dict_.items():
            self[key] = value

    def __getattr__(self, attr):
        return self[attr]

    def __setitem__(self, attr, value):
        if isinstance(value, dict):
            value = AttributeDict(value)
        super().__setitem__(attr, value)

