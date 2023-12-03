import time
from datetime import datetime
script_start_time = datetime.now()

start_time = time.time()

MINIMUM = 32

def find_minrun(n):
    r = 0
    while n >= MINIMUM:
        r |= n & 1
        n >>= 1
    return n + r

def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        j, element = i - 1, array[i]
        while j >= left and element < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = element
    return array

def merge(array, l, m, r):
    left, right = array[l:m+1], array[m+1:r+1]
    i = j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    array[k:r+1] = left[i:] + right[j:]

def tim_sort(array):
    n = len(array)
    minrun = find_minrun(n)

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        insertion_sort(array, start, end)

    size = minrun
    while size < n:
        for left in range(0, n, 2 * size):
            mid, right = min(n - 1, left + size - 1), min(left + 2 * size - 1, n - 1)
            merge(array, left, mid, right)
        size *= 2

array = [-1, 5, 0, -3, 11, 9, -2, 7, 0]
print("Array:")
print(array)
tim_sort(array)
print("Sorted Array:")
print(array)

# print("Process finished --- %s seconds ---" % (time.time() - st))
end_time = time.time()
final_time = end_time - start_time
print(final_time)
script_end_time = datetime.now()
print(script_end_time - script_start_time )