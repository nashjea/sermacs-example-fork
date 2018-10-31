"""
molssi_math.py
Example repository for MolSSI Workshop at SERMACS 2018

This file contains a function to compute the mean of a list
"""


def mean(num_list):
    """
    Calculate the mean/average of a list of numbers

    Parameters
    ------------------
    num_list : list
        The list to take the average of

    Returns
    -------------------
    ret: float
        The mean of the list

    Examples
    --------------------
    >>> mean([1, 2, 3, 4, 5])
    3.0
    """

    ret = sum(num_list)/len(num_list)

    return ret
