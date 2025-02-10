# calculator/calculations.py
from pydantic import Field, validate_call
from typing_extensions import Annotated

"""
Provide several sample math calculations.

This module allows the user to make mathematical calculations.

Examples
--------
>>> from calculator import calculations
>>> calculations.add(2, 4)
6.0
>>> calculations.multiply(2.0, 4.0)
8.0
>>> from calculator.calculations import divide
>>> divide(4.0, 2)
2.0

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""


@validate_call
def add(a: Annotated[float | int, Field(gt=0)], b: float | int) -> float | int:
    """
    Add two numbers.

    Examples
    --------
    >>> add(4.0, 2.0)
    6.0
    >>> add(4, 2)
    6.0

    Parameters
    ----------
    a : float
        The first number to add.
    b : float
        The second number to add.

    Returns
    -------
    float
        A number representing the arithmetic sum of `a` and `b`.
    """
    return a + b


def subtract(a, b):
    """
    Subract one number from another

    Examples
    --------
    >>> subtract(4.0, 2.0)
    2.0
    >>> subtract(4, 2)
    2.0

    Parameters
    ----------
    a : float
        The number to subtract from.
    b : float
        The number to subtract.

    Returns
    -------
    float
        A number representing the arithmetic difference of `a` and `b`.
    """
    return float(a - b)


def multiply(a, b):
    """
    Multiply two numbers.

    Examples
    --------
    >>> multiply(4.0, 2.0)
    8.0
    >>> multiply(4, 2)
    8.0

    Parameters
    ----------
    a : float
        The first number to multiply.
    b : float
        The second number to multiply.

    Returns
    -------
    float
        A number representing the arithmetic multiplication of `a` and `b`.
    """
    return float(a * b)


def divide(a, b):
    """
    Divide one number by another

    Examples
    --------
    >>> divide(4.0, 2.0)
    2.0
    >>> divide(4, 2)
    2.0

    Parameters
    ----------
    a : float
        The number to divide.
    b : float
        The number to divide by.

    Returns
    -------
    float
        A number representing the arithmetic division of `a` and `b`.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")

    return float(a / b)
