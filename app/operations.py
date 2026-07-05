import logging

logger = logging.getLogger(__name__)

def add(a, b):
    logger.info("Adding %s and %s", a, b)
    return a + b

def subtract(a, b):
    logger.info("Subtracting %s and %s", a, b)
    return a - b

def multiply(a, b):
    logger.info("Multiplying %s and %s", a, b)
    return a * b

def divide(a, b):
    logger.info("Dividing %s by %s", a, b)
    if b == 0:
        logger.error("Division by zero attempted")
        raise ValueError("Cannot divide by zero!")
    return a / b