import time

def insertion_sort(l, left=0, right=None):
    if right is None:
        right = len(l) - 1

    for i in range(left + 1, right + 1):
        key = l[i]
        j = i - 1
        while j >= left and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l

def merge(array, l, m, r):
    left, right = array[l:m + 1], array[m + 1:r + 1]
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
    array[k:r + 1] = left[i:] + right[j:]

def tim_sort(l):
    min_run = 10
    n = len(l)

    for i in range(0, n, min_run):
        insertion_sort(l, i, min((i + min_run - 1), (n - 1)))

    size = min_run
    while size < n:
        for s in range(0, n, size * 2):
            mid = s + size - 1
            end = min((s + size * 2 - 1), (n - 1))

            merge(l, s, mid, end)

        size *= 2
    return l

start_time = time.time()
l1 = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 60, 76, 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]
print(l1)
res = tim_sort(l1)
print()
print(res)
print(time.time() - start_time)