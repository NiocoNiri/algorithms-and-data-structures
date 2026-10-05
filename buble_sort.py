


def buble_sort(a):
    for i in range(len(a)-1):
        for z in range(1,len(a)-i):
            if a[z-1] > a[z]:
                a[z-1], a[z] = a[z], a[z-1]
    return(a)

       

