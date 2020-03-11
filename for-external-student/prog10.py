from random import shuffle
import sys
import time 

sys.setrecursionlimit(15000)


def get_array(name_file):
    with open(name_file, 'r') as f:
        return list(map(int, f.readlines()[0].split()))

def sorting_by_shoice(arr):
    n = len(arr)
    for r in range(n, 0, -1):
        pos_max = 0
        for j in range(r):
            if arr[j] > arr[pos_max]:
                pos_max = j
        arr[r-1], arr[pos_max] = arr[pos_max], arr[r-1]
    return arr


def sorting_by_shoice_rec(arr):
    if len(arr) < 1:
        return []
    else:
        pos_max = arr.index(max(arr))
        arr[-1], arr[pos_max] = arr[pos_max], arr[-1]
        return sorting_by_shoice_rec(arr[:-1]) + [arr[-1]]


def quick_sorting(arr):
    if len(arr) < 2:
        return arr
    else:
        pos_mid = len(arr)//2
        mid = arr[pos_mid]
        l_arr = list(filter(lambda item: item<=mid, arr))
        r_arr = list(filter(lambda item: item>mid, arr))
    return quick_sorting(l_arr[:-1]) + [l_arr[-1]] + quick_sorting(r_arr)

arr = get_array('numbers.txt')
# print(*arr)

# shuffle(arr)
# print(*arr)

start = time.monotonic()

# sort_arr = sorting_by_shoice(arr)
# sort_arr = sorting_by_shoice_rec(arr)
sort_arr = quick_sorting(arr)

finish = time.monotonic()
print("%.3f" % (finish-start))

# print(*sort_arr)