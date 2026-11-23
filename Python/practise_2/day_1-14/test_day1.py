import pytest

from day1 import (
    normalize_value,
    add_item,
    clone_config,
)


@pytest.fixture
def config():
    return {
        "app": "monitor",
        "settings": {
            "theme": "dark",
            "features": ["cpu", "memory"]
        }
    }   


@pytest.mark.parametrize("val", (1, 1.1, True))
def test_normalize_value(val):
    result = normalize_value(val)

    assert result == val


@pytest.mark.parametrize("val", (None, ""))
def test_normalize_value_none(val):
    result = normalize_value(val)

    assert result == None


@pytest.mark.parametrize("val", (" ", "\n", "123", "   123", "123   ", "  123 "))
def test_normalize_value_string(val):
    result = normalize_value(val)

    assert result == val.strip()


@pytest.mark.parametrize("val", ([1,2], {"1":1}))
def test_normalize_value_unsupported_type(val):
    with pytest.raises(TypeError):
        result = normalize_value(val)


def test_add_item():
    result = add_item(1)

    assert result == [1]

    result = add_item(2)
    assert result == [2]


def test_clone_config_default(config):
    result = clone_config(config)
    assert result == config

    config['app'] = "test"
    config['settings']['theme'] = 'default'

    # no change
    assert result['app'] != "test"
    assert result['app'] == "monitor"

    # changed
    assert result['settings']['theme'] == "default"


def test_clone_config_shallow(config):
    result = clone_config(config, deep=False)
    assert result == config

    config['app'] = "test"
    config['settings']['theme'] = 'default'

    # no change
    assert result['app'] != "test"
    assert result['app'] == "monitor"

    # changed
    assert result['settings']['theme'] == "default"


def test_clone_config_deep(config):
    result = clone_config(config, deep=True)
    assert result == config

    config['app'] = "test"
    config['settings']['theme'] = 'default'

    # no change
    assert result['app'] != "test"
    assert result['app'] == "monitor"

    assert result['settings']['theme'] != "default"
    assert result['settings']['theme'] == "dark"
