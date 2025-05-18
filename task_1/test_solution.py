import pytest
from solution import sum_two, strict


def test_sum_two_valid():
    assert sum_two(1, 2) == 3


def test_sum_two_invalid_type():
    with pytest.raises(TypeError):
        sum_two(1, 2.4)


def test_sum_two_invalid_type_str():
    with pytest.raises(TypeError):
        sum_two("1", 2)


@strict
def concat_strings(a: str, b: str) -> str:
    return a + b


def test_concat_strings_valid():
    assert concat_strings("hello", "world") == "helloworld"


def test_concat_strings_invalid_type():
    with pytest.raises(TypeError):
        concat_strings("hello", 123)
