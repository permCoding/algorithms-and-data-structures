import random

def generator(count = 10, num_min = 0, num_max = 100):
    return [random.randint(num_min, num_max) for _ in range(count)]

steps = 0
def binary_find(num, arr):
    global steps
    l = 0; r = len(arr) - 1
    while l <= r:
        middle = (l+r)//2
        if num == arr[middle]:
            return True
        if num > arr[middle]:
            l = middle + 1
        else:
            r = middle - 1
        steps += 1
    return False

arr = generator(2000)
arr = sorted(arr)
with open('numbers.txt', 'w') as f:
    f.write(' '.join(list(map(str, arr))))

# arr = []
# with open('numbers.txt', 'r') as f:
#     arr = list(map(int, f.readlines()[0].split()))

# print(*arr)
# print(binary_find(98, arr))
# print(steps)