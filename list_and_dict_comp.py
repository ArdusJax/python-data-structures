arr = [1, 2, 13, 44, 5, 33, 1, 21, 5, 19, 77, 9, 393, 1, 2, 99]


# Even numbers
def evens(arr):
    even_list = [x for x in arr if x % 2]
    print(even_list)


# evens(arr)


# Odds
def odds(arr):
    odd_list = [x for x in arr if not x % 2]
    print(odd_list)


# odds(arr)


d = {1: "one", 2: "two", 3: "three", 4: "four"}


def find(key: int, d):
    found = {k: v for k, v in d.items() if k == key}
    print(f"{found}")


find(2, d)
find(3, d)
find(4, d)
