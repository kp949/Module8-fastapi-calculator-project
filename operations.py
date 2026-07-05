"""Basic arithmetic functions used by the FastAPI routes."""

import logging
from typing import Union

logger = logging.getLogger(__name__)
Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    logger.info("Adding %s and %s", a, b)
    return a + b


def subtract(a: Number, b: Number) -> Number:
    logger.info("Subtracting %s and %s", a, b)
    return a - b


def multiply(a: Number, b: Number) -> Number:
    logger.info("Multiplying %s and %s", a, b)
    return a * b


def divide(a: Number, b: Number) -> float:
    logger.info("Dividing %s by %s", a, b)
    if b == 0:
        logger.error("Division by zero attempted")
        raise ValueError("Cannot divide by zero!")
    return a / b
