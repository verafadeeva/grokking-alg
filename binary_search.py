import time
import random


def binary_search(sorted_sequence, item):
    low = 0
    high = len(sorted_sequence) - 1
    while low < high:
        mid = (low + high) // 2
        guess = sorted_sequence[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        elif guess > item:
            high = mid
    return None


data = [
    (1, range(100), random.randint(1, 100)),
    (2, range(1000000), random.randint(1, 999999)),
    (3, range(1000000000), random.randint(1, 1000000000)),
    (4, range(100), random.randint(100, 1000))
]


def main():
    for i, sequence, item in data:
        try:
            start = time.time()
            index = binary_search(sequence, item)
            finish = time.time()
        except Exception as error:
            print(error)
        finally:
            print(f'{i}: index: {index}; item: {item}; time: {finish - start}')


if __name__ == '__main__':
    main()
