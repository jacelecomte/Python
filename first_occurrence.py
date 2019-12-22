# With runtime of O(log n) print array position of the first '1' found in the array

def location_of_first_one(array):
    counter = 0
    lowerbound = 0
    upperbound = 0
    length = len(array)

    if length == 1:
        return 0

    while counter < length:
        lowerbound = counter
        counter *= 2
        upperbound = counter
        if upperbound > length:
            upperbound = upperbound - 1
        if array[lowerbound] == array[upperbound]:
            counter = lowerbound + 1
        elif array[lowerbound] != array[upperbound]:
            if array[upperbound] == array[upperbound - 1]:
                return upperbound-1
            return upperbound
        else:
            print("error")
    return 'error'

n = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
o = [1]
p = []

print(location_of_first_one(n))
print(location_of_first_one(m))
print(location_of_first_one(o))
print(location_of_first_one(p))

