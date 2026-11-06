def max_contiguous(lst):
    if not isinstance(lst, list):
        raise TypeError
    
    if len(lst) == 0:
        return 0

    curmax = lst[0]
    totalmax = lst[0]

    for i in range(1,len(lst)):
        curmax += lst[i]
        if lst[i] > curmax:
            curmax = lst[i]
        if curmax > totalmax:
            totalmax = curmax

    return totalmax


def max_contiguous(lst):
    if not isinstance(lst, list):
        raise TypeError
    
    if len(lst) == 0:
        return 0

    curmax = lst[0]
    totalmax = lst[0]

    for i in range(1,len(lst)):
        curmax += lst[i]
        if lst[i] > curmax:
            curmax = lst[i]
        totalmax = curmax

    return totalmax

def max_contiguous(lst):
    if not isinstance(lst, list):
        raise TypeError
    
    if len(lst) == 0:
        return 0

    curmax = lst[0]
    totalmax = lst[0]

    for i in range(len(lst)-1,-1,-1):
        curmax += lst[i]
        if lst[i] > curmax:
            curmax = lst[i]
        if curmax > totalmax:
            totalmax = curmax

    return totalmax


def max_contiguous(lst):
    if not isinstance(lst, list):
        raise TypeError
    
    if len(lst) == 0:
        return 0

    curmax = lst[0]
    totalmax = lst[0]

    for i in range(len(lst)-1,0,-1):
        curmax += lst[i]
        if lst[i] > curmax:
            curmax = lst[i]
        if curmax > totalmax:
            totalmax = curmax

    return totalmax

def max_contiguous(lst):
    if not isinstance(lst, list):
        raise TypeError
    
    if len(lst) == 0:
        return -1

    curmax = lst[0]
    totalmax = lst[0]

    for i in range(1,len(lst)):
        curmax += lst[i]
        if lst[i] > curmax:
            curmax = lst[i]
        if curmax > totalmax:
            totalmax = curmax

    return totalmax

def max_contiguous(lst):
    if not isinstance(lst, list):
        raise TypeError
    
    if len(lst) == 0:
        return 1

    curmax = lst[0]
    totalmax = lst[0]

    for i in range(1,len(lst)):
        curmax += lst[i]
        if lst[i] > curmax:
            curmax = lst[i]
        if curmax > totalmax:
            totalmax = curmax

    return totalmax


def max_contiguous(lst):
    if not isinstance(lst, list):
        raise TypeError
    
    if len(lst) == 0:
        return 0

    curmax = 0
    totalmax = 0

    for i in range(1,len(lst)):
        curmax += lst[i]
        if lst[i] > curmax:
            curmax = lst[i]
        if curmax > totalmax:
            totalmax = curmax

    return totalmax


def max_contiguous(lst):
    if not isinstance(lst, list):
        raise TypeError
    
    if len(lst) == 0:
        return 0

    curmax = -1
    totalmax = 0

    for i in range(1,len(lst)):
        curmax += lst[i]
        if lst[i] > curmax:
            curmax = lst[i]
        if curmax > totalmax:
            totalmax = curmax

    return totalmax


def max_contiguous(lst):
    if not isinstance(lst, list):
        raise TypeError
    
    if len(lst) == 0:
        return 0

    curmax = -100
    totalmax = -100

    for i in range(1,len(lst)):
        curmax += lst[i]
        if lst[i] > curmax:
            curmax = lst[i]
        if curmax > totalmax:
            totalmax = curmax

    return totalmax


def max_contiguous(lst):
    if not isinstance(lst, list):
        raise TypeError
    
    if len(lst) == 0:
        return 0

    curmax = 100
    totalmax = 100

    for i in range(1,len(lst)):
        curmax += lst[i]
        if lst[i] > curmax:
            curmax = lst[i]
        if curmax > totalmax:
            totalmax = curmax

    return totalmax


def max_contiguous(lst):
    if not isinstance(lst, list):
        raise TypeError
    
    if len(lst) == 0:
        return 0

    curmax = -5
    totalmax = -5

    for i in range(1,len(lst)):
        curmax += lst[i]
        if lst[i] > curmax:
            curmax = lst[i]
        if curmax > totalmax:
            totalmax = curmax

    return totalmax


def max_contiguous(lst):
    if not isinstance(lst, list):
        raise TypeError
    
    if len(lst) == 0:
        return 0

    curmax = 1
    totalmax = 1

    for i in range(1,len(lst)):
        curmax += lst[i]
        if lst[i] > curmax:
            curmax = lst[i]
        if curmax > totalmax:
            totalmax = curmax

    return totalmax