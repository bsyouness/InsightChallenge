""" This is a library for computing a running median. 

This code is based on this discussion:
http://stackoverflow.com/questions/10657503/find-running-median-from-a-stream-of-integers

It works by maintaining two heaps, one for the elements smaller than the median and one for
the elements larger than the median. The complexity for running the algorithm over n elements 
is O(nlog(n)).
"""

from heapq import heappop, heappush

def running_median_next_step(left_heap, right_heap, x):
    """ This computes the next step in the running median computation. 

    We assume three invariants:
    1) The left_heap's elements are all smaller than or equal to the right_heap's,
    2) The numbers of elements in the heaps differ by at most one. We call this "balanced".
    3) right_heap contains at least as many elements as left_heap.

    Args:
      left_heap: A max heap of numbers.
      right_heap: A min heap of numbers.
      x: The next number to consider in the running median computation. 

    Returns:
      A list containing updated heaps and the new median.
    """

    # Add the new element to the appropriate heap.
    if len(right_heap) == 0 or x >= right_heap[0]:
        heappush(right_heap, x)
    else:
        heappush(left_heap, -x)

    # Ensure the heaps are balanced. 
    if len(right_heap) < len(left_heap):
        heappush(right_heap, -heappop(left_heap))
    elif len(right_heap) - len(left_heap) == 2:
        heappush(left_heap, -heappop(right_heap))

    # Calculate the median. 
    if len(right_heap) > len(left_heap):
        median = right_heap[0]
    else:
        median = (right_heap[0] - left_heap[0]) / float(2)

    return [left_heap, right_heap, median]


def running_median(numbers):
    """ This takes in an iterator of numbers and returns an iterator which is the running median.

    Args:
      numbers: An iterator of numbers.

    Returns:
      This returns an iterator which is the running median.
    """
    left_heap = []
    right_heap = []
    for n in numbers:
        [left_heap, right_heap, median] = running_median_next_step(left_heap, right_heap, n)
        yield median