import pytest
from cognite.air.utils import is_jsonable, strip_patch_from_version


@pytest.mark.parametrize("val", ("test", 2))
def test_is_jsonable__not_valid(val):
    assert not is_jsonable(val)


def test_is_jsonable__valid():
    assert is_jsonable('{"key1": "value1", "key2": "value2"}')


def test_strip_patch_from_version__not_valid_version_typeerror():
    with pytest.raises(TypeError):
        strip_patch_from_version(2)


@pytest.mark.parametrize("version", ("1.2.3.4", "1.2...5"))
def test_strip_patch_from_version__not_valid_version_valueerror(version):
    with pytest.raises(ValueError):
        strip_patch_from_version(version)


@pytest.mark.parametrize("version_str", ("2.2", "2.2.1"))
def test_strip_patch_from_version__valid_version(version_str):
    assert strip_patch_from_version(version_str) == "2.2"
