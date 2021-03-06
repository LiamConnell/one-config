import sys

import yaml

__all__ = ['build_config', 'get_config', 'ConfigError']


class ConfigError(Exception):
    pass


_CONFIG_DATA = {}


def build_config(name: str = sys.argv[0]):
    if _CONFIG_DATA.get(name):
        raise ConfigError('This config has already been constructed')
    return ConfigBuilder(name)


def get_config(name: str = sys.argv[0]):
    try:
        return _CONFIG_DATA[name]
    except KeyError:
        raise ConfigError('This config has not been constructed yet')


class ConfigBuilder:
    def __init__(self, config_key: str):
        self.config_key = config_key

    def from_yaml(self, path):
        with open(path, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        data = AttributeDict(data)
        _CONFIG_DATA[self.config_key] = data
        return data


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

