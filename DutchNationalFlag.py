#Dijkstra's Dutch National Flag Problem - O(n) runtime.
#Scanning through an array of unsorted red, white, and blue colors, sort so all the red are first, then blue, then white.
def dutch_sort(a = []):
    lower,middle,high=0,0,len(a)-1
    redcount,whitecount,bluecount=0,0,0
    print ("Given array of " + str(a) + ", has counts of:")
    while middle<=high:
        if a[middle] == 0:
            a[lower],a[middle] = a[middle],a[lower]
            lower += 1
            middle += 1
            redcount += 1
        elif a[middle] == 1:
            middle += 1
            whitecount += 1
        else:
            a[middle],a[high] = a[high],a[middle]
            high -= 1
            bluecount += 1
    print("# of Red = "+str(redcount)+", # of White = " + str(whitecount) + ", # of Blue = "+str(bluecount))
    print("and is sorted as:")
    print (a)
    return a

g = [0, 0, 1, 1, 2, 2]
h = [0, 1, 2, 0, 1, 2]
i = [0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 0, 1, 2, 0, 1, 2]
j = [0]
k = [1]
l = [2]

print (dutch_sort(g), dutch_sort(h), dutch_sort(i), dutch_sort(j), dutch_sort(k), dutch_sort(l))

#This algorithm is based on a more complex version of the triple sort algorithm.
def triplesort(a = []):
    if (a[0] < a[2]) and (a[1] < a[2]):
        if a[1] < a[0]:
            return a[1],a[0],a[2]
        return a[0],a[1],a[2]
    if (a[0] < a[1]) and (a[2] < a[1]):
        if a[0] < a[2]:
            return a[0],a[2],a[1]
        return a[2],a[0],a[1]
    if (a[1] < a[0]) and (a[2] < a[0]):
        if a[1] < a[2]:
            return a[1],a[2],a[0]
        return a[2],a[1],a[0]
    return -1

a = [0,1,2]
b = [0,2,1]
c = [1,0,2]
d = [1,2,0]
e = [2,1,0]
f = [2,0,1]
#print (triplesort(a), triplesort(b), triplesort(c), triplesort(d), triplesort(e), triplesort(f))



