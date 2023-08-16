#!/usr/bin/python3
"""
This module is composed by a function that adds two numbers
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns their sum.
    Args:
        a: An integer or float to be added
        b: An integer or float to be added (default value is 98)
    Returns:
        An integer representing the sum of a and b
    Raises:
        TypeError: If a or b is not an integer and/or float
    """
    # Check if a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # Add the integers a and b
    result = a + b

    #dd_integer` Module
==========================

This module provides a function `add_integer` that adds two numbers.

Using `add_integer`
-------------------

Importing the function from the module:
>>> add_integer = __import__('0-add_integer').add_integer

Addition Examples:
>>> add_integer(5, 3)
8

>>> add_integer(-50, -50)
-100

>>> add_integer(-10, 5)
-5

>>> add_integer(2.0, 4.0)
6

>>> add_integer(2)
100

Handling Invalid Inputs:
>>> add_integer(10, "two")
Traceback (most recent call last):
    ...
TypeError: b must be an integer

>>> add_integer(None)
Traceback (most recent call last):
    ...
TypeError: a must be an integer

>>> add_integer('1', 5)
Traceback (most recent call last):
    ...
TypeError: a must be an integer

>>> add_integer('abc', 'def')
Traceback (most recent call last):
    ...
TypeError: a must be an integer

>>> add_integer((1, 2, 3))
Traceback (most recent call last):
    ...
TypeError: a must be an integer

>>> add_integer(10, [1, 2, 3])
Traceback (most recent call last):
    ...
TypeError: b must be an integer

>>> add_integer("Hello")
Traceback (most recent call last):
    ...
TypeError: a must be an integer

Special Cases:
>>> add_integer(float('inf'), 0)
Traceback (most recent call last):
    ...
OverflowError: cannot convert float infinity to integer

>>> add_integer(float('inf'), float('-inf'))
Traceback (most recent call last):
    ...
OverflowError: cannot convert float infinity to integer

>>> add_integer(0, float('nan'))
Traceback (most recent call last):
    ...
ValueError: cannot convert float NaN to integer Return the sum of a and b
    return result
