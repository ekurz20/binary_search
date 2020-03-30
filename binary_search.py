#!/bin/python3

def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT: 
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    alist = xs
    first = 0
    last = len(alist)-1
    if len(alist) == 0:
        return None
    if len(alist) == 1:
        if alist[0] >0:
            return 0
        else:
            return None
    if len(alist)==2:
        if alist[0]>0:
            return 0
        elif alist[0] == 0:
            if alist[1] > 0:
                return 1
            else:
                return None
        elif alist[0]<0:
            if alist[1] == 0 or alist[1]<0:
                return None
            else:
                return 1
    while first <= last:
        if last == 0:
            return last
        if first == last and alist[first] > 0:
            return last
        if first == last and alist[first] < 0:
            return None
        midpoint = (first+last)//2
        if alist[midpoint] == 0:
            return midpoint + 1
        else:
            if 0<alist[midpoint]:
                last = midpoint
            else:
                first = midpoint

def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT: 
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2

    I highly recommend creating stand-alone functions for steps 1 and 2
    that you can test independently.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''
    alist = xs
    item = x
    if alist == []:
        return 0
    if len(alist)==1 and alist[0]!=item:
        return 0
    if binarySearch(alist,item) == False:
        return 0

    first = 0
    last = len(alist)-1
    if alist[first]==alist[last]:
        return last-first+1
    if alist[first]==item and alist[first+1]!=item:
        return 1

    upper = upperbinarySearch(alist, item)
    lower = lowerbinarySearch(alist, item)
    return upper - lower + 1




def upperbinarySearch(alist,item):
    first = 0
    last = len(alist)-1

    if alist[last]==item:
        return last
    while first<=last:
        midpoint = (first+last)//2
        if alist[midpoint] < item & alist[midpoint-1]==item:
            return midpoint-1
        else:
            if item > alist[midpoint]:
                last = midpoint -1
            else:
                first = midpoint+1

def lowerbinarySearch(alist,item):
    first = 0
    last = len(alist)-1
    found = False

    if alist[first]==item:
        return first
    while first <= last and not found:
        midpoint = (first+last)//2
        if alist[midpoint]>item and alist[midpoint+1]==item:
            found = True
            return midpoint + 1
        else:
            if item < alist[midpoint]:
                first = midpoint + 1
            else:
                last = midpoint -1

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first <=last and not found:
        midpoint = (first+last)//2
        if alist[midpoint]==item:
            found = True
        else:
            if item > alist[midpoint]:
                last = midpoint -1
            else:
                first = midpoint +1
    return found

def argmin(f, lo, hi, epsilon):
    '''
    Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest, 
               you recursively call your function on the interval [lo,m2] or [m1,hi]

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''
    f = f
    epsilon = epsilon
    hi = hi
    lo = lo
    found = False

    while (hi-lo)>epsilon:
        m1=(hi-lo)/3+lo
        m2=2*(hi-lo)/3+lo
        if f(lo)<f(m1):
            hi=m1
        elif f(m1)<f(m2):
            hi = m2
        elif f(m2)<f(m1):
            lo = m1
    return (hi+lo)/2
