
def fast_sort(a):
    if len(a) <= 1:
        return a
    p = a[len(a) // 2]
    l = [x for x in a if x < p]
    m = [x for x in a if x == p]
    r = [x for x in a if x > p]
    return fast_sort(l) + m + fast_sort(r)
