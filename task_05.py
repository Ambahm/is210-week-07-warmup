#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Replacing for indexes in reverse"""

def flip_keys(to_flip):

    """Functionreverses iner items in reverse order

    Arg:
        to_flip (list): Nested list of immutables.

    Return:
        Original list with inner items reversed.

    Example:

        >>> flip_keys([(1, 2, 3), 'abc'])
        [(3, 2, 1), 'cba']

    """

    count_limit = len(to_flip)

    for nth in range(count_limit):

        # For nth item in list its sub nth element is reversed
        to_flip[nth] = to_flip[nth][::-1]

    return to_flip
