from random import randint
a = []
for i in range (0,100):
   a.append(randint(1,99))

for i in range(len(a)-1):
    for z in range(1,len(a)-i):
        if a[z-1] > a[z]:
            a[z-1], a[z] = a[z], a[z-1]


       
if a == sorted(a):
    print("Done") 
else:
    print(a)