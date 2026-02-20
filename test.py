import sys


def test(left, right):
    if (left != right):
        raise AssertionError()


sys.modules[__name__] = test