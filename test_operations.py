import pytest

from app.operations import add, divide, multiply, subtract


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(2, 3, 5), (-1, 5, 4), (2.5, 1.5, 4.0)],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(8, 3, 5), (3, 8, -5), (5.5, 1.5, 4.0)],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(4, 5, 20), (-2, 6, -12), (2.5, 2, 5.0)],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(9, 3, 3), (7, 2, 3.5), (-8, 2, -4)],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)
