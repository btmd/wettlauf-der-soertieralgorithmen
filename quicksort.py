# heaviliy borrowed from https://pythonic-interviews.readthedocs.io/en/latest/_modules/src/classic_algo/sort.html

from array import *
import time
import random

def quick_sort(a):
    """
    Another divide and conquer algorithm, quick sort relies on choosing a pivot
    value. The list is then partitioned using the scheme described in
    partition_helper. This placed the
    pivot in its correct position in the sorted list, the function is then
    called on the sublist a[:right_mark - 1] and a[right_mark+1:]
    """
    if len(a) <= 1:
        return a
    quicksort_helper(a, 0, len(a) - 1)
    return a



def quicksort_helper(a, first, last):
    """
    Helper function splitting the list at the pivot and recursively calling
    itself on the left and right parts of this splitpoint.
    """
    if first < last:
        split_point = partition_helper(a, first, last)
        quicksort_helper(a, first, split_point - 1)
        quicksort_helper(a, split_point + 1, last)



def partition_helper(a, first, last):
    """
    A left_mark index are initiated at the leftmost index available (ie
    not the pivot) and a right_mark at the rightmost. The left_mark is shifted
    right as long as a[left_mark] < pivot and the right_mark left as long as
    a[right_mark] > pivot. If left_mark < right_mark, the values at which the
    marks are stopped are swaped and the process continues until they cross.
    At this point, a[right_mark] and the pivot are swapped and the index of the
    right_mark is returned.
    """
    pivot_value = a[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while right_mark >= left_mark and a[left_mark] <= pivot_value:
            left_mark += 1

        while right_mark >= left_mark and a[right_mark] >= pivot_value:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            a[left_mark], a[right_mark] = a[right_mark], a[left_mark]

    a[first], a[right_mark] = a[right_mark], a[first]
    return right_mark



'''
Put your programm here
all print() and variable declarations! (x = 5 or date_before = int(round(blablabla)) are variable declarations)
"""
