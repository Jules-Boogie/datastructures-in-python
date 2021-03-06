"""
Module to show off tuple methods.

Neither this module nor the function should import the introcs module.  In addition,
the function should not use a loop or recursion.

Author: Juliet George
Date: 8/24/2020
"""


def replace_first(tup,a,b):
    """
    Returns a copy of tup with the first value of a replaced by b

    Examples:
        replace_first((1,2,1),1,3) returns (3,2,1)
        replace_first((1,2,1),4,3) returns (1,2,1)

    Parameter tup: The tuple to copy
    Precondition: tup is a tuple of integers

    Parameter a: The value to replace
    Precondition: a is an int

    Parameter b: The value to replace with
    Precondition: b is an int
    """
    try:
      test = tup.index(a)
      arr = list(tup)
      arr.pop(test)
      arr.insert(test,b)
      return tuple(arr)
    except ValueError:
      return tup
