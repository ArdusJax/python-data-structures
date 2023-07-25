from collections import defaultdict
import re
from typing import DefaultDict

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


def count_words(string):
    counts = DefaultDict(int)
    for word in re.findall("\w+", string):
        counts[word] += 1
    print(counts)


s = "This is a sentence that has a lot of words in it. Please count all the words"
count_words(s)


def add_or_insert(string):
    words = string.split(" ")
    count = DefaultDict(int)
    for item in words:
        if item in count.keys():
            count[item] += 1
        else:
            count[item] = 1
    print(f"Add or insert: {count}")


add_or_insert(s)
