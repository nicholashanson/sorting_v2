def quicksort_(data,lo,hi):

    if lo >= hi or lo < 0:
        return

    g = partition( data, lo, hi )

    for i in g:
        p = i[1]

    yield quicksort_( data, lo, p - 1 )  
    yield quicksort_( data, p + 1, hi )

def partition(data,lo,hi):

    pivot = data[hi]

    i = lo

    for j in range( lo, hi ):
        yield data, i, j, False

        if data[j] <= pivot:
            yield data, i, j, True
            data[i], data[j] = data[j], data[i]
            i += 1

    data[i], data[hi] = data[hi], data[i]

    return i