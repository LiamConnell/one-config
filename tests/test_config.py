import pytest

import one_config


def test_config__cross_module():
    CONFIG = one_config.get_config()
    assert CONFIG.test == 'pass'


def test_config__name():
    one_config.build_config('test_name').from_yaml('configs/test_name.yaml')
    CONFIG = one_config.get_config('test_name')
    assert CONFIG.test.name == 'pass'

    CONFIG_2 = one_config.get_config()
    assert CONFIG_2.test == 'pass'


def test_config__multiple_config_error():
    with pytest.raises(one_config.ConfigError):
        one_config.build_config().from_yaml('configs/test_name.yaml')