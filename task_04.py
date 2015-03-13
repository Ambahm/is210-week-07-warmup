#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""To create a function for list or tuple addition and average"""

def process_data(data):
    """Functon takes input and gives total sum and  average of the data

    Args:
        data (mixed): A list or tuple of numbers

    Returns:
        tuple: a tuple for the total sum and the average,
        with floating point precision and rounded to two digits

    Example:
        >>> process_data([3.3,33.9])
        (37.2, 18.6)

        >>> process_data([1,2,3])
        (6.0, 2.0)

    """
    number_add = 0          # Assigning variable for total of numbers

    for count in data:      # loop to continue to the extend of items entered
        number_add += count # add until the loop is continued

    number_avg = round((number_add / float(len(data))), 2)

    return (round(number_add, 2), number_avg)

