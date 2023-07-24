from typing import List

# test array
arr = [1, 2, 13, 44, 5, 33, 1, 21, 5, 19, 77, 9, 393, 1, 2, 99]


def bubble_sort(a: List[int]):
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp

    print(a)


bubble_sort(arr)
