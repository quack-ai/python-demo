from packaging.version import parse

import my_lib


def test_version():
    # Check that the attribute exists
    assert isinstance(getattr(my_lib, "__version__"), str)
    # Check that the string isn't corrupted
    version = parse(my_lib.__version__)
    # 3 part version string
    assert len(version.release) == 3
    # Dev build
    assert isinstance(version.dev, int)
