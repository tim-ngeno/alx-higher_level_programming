#!/usr/bin/python3
"""Find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Defines an algorithm to find a peak in a list of unsorted
    integers

    Arguments:
        list_of_integers (list):  a list of integers
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        # Check if the mid element is less than its next neighbor.
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1

        # Otherwise, the peak is on the left side.
        else:
            high = mid

    # low and high will converge to a peak element.
    return list_of_integers[low]
