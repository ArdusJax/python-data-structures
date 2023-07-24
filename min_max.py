def min_max_sum(arr):
    min = arr[0]
    max = arr[0]
    total = 0

    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]

        total = total + arr[i]

    print(f"total: {total}  max: {max} min: {min}")


arr = [1, 2, 13, 44, 5, 33, 1, 21, 5, 19, 77, 9, 393, 1, 2, 99]

print(f"Sample data:\n{arr}")
min_max_sum(arr)
