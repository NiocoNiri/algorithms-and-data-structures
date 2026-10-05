from random import randint
a = []
for i in range (0,10):
   a.append(randint(1,10))
def quicksort_demo(a):
    if len(a) <= 1:
        return a
    p = a[len(a) // 2]
    l = [x for x in a if x < p]
    m = [x for x in a if x == p]
    r = [x for x in a if x > p]
    return quicksort_demo(l) + m + quicksort_demo(r)
if quicksort_demo(a) == sorted(a):
   print("Done")
else:
   print(a)