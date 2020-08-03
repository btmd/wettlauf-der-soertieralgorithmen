# heavily borrowed from https://pythonic-interviews.readthedocs.io/en/latest/_modules/src/classic_algo/sort.html
# most inefficient sorting algorithm

from array import *
import time
###import random


def bubble_sort(a):
    """
    In this algo, the i-th pass starts at the first element and compare
    sequencially each element to the next, swapping them if necessary, up to
    n-i. The biggest element 'bubbles up' to the n-i position. This runs in
    O(n^2): n-1 passes of O(n) comparisons.

    Note the use of the pythonic swap operation "a, b = b, a", not requiring
    the use of a temporary storage variable.
    """
    length = len(a)
    for pass_number in range(length):
        for i in range(1, length - pass_number):
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]
    return a


# declare array with integers only ('i')
my_array = array('i',[12,1,299,172,152,187,0,1000])

###3my_array = [random.randint(1,1000000) for _ in range(100000)]

print(*my_array)
time_before = int(round(time.time() * 1000))
print(time_before)
print(*bubble_sort(my_array))
time_after = int(round(time.time() * 1000))
print(time_after)
print("time difference (in ms)")
print(time_after - time_before)
