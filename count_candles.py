def count_candles(arr):
    candle_counts = {}
    for i in range(len(arr)):
        if arr[i] not in candle_counts.keys():
            candle_counts[arr[i]] = 1
        else:
            candle_counts[arr[i]] = candle_counts[arr[i]] + 1

    print(candle_counts)


arr = [1, 2, 13, 44, 5, 33, 1, 21, 5, 19, 77, 9, 393, 1, 2, 99]
count_candles(arr)
