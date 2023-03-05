import time
import random


# Пример из книжки через цикл

def binary_search_loop(sorted_sequence, item):
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


# Реализация через рекурсию (неудобно, что нужно сразу знать размер массива)

def binary_search_rec(sorted_sequence, item, left, right):
    mid = (left + right) // 2
    if left > right:
        return -1
    if item == sorted_sequence[mid]:
        return mid
    if item < sorted_sequence[mid]:
        return binary_search_rec(sorted_sequence, item, left, mid-1)
    return binary_search_rec(sorted_sequence, item, mid+1, right)


# Но можно обернуть в функцию

def binary_search(sorted_sequence, item):
    result = binary_search_rec(
        sorted_sequence, item, 0, len(sorted_sequence)-1)
    return result


data = [
    (1, range(100), random.randint(1, 100)),
    (2, range(1000000), random.randint(1, 999999)),
    (3, range(1000000000), random.randint(1, 1000000000)),
    (4, range(100), random.randint(100, 1000))
]


def main():
    for i, sequence, item in data:
        try:
            start1 = time.time()
            index1 = binary_search_loop(sequence, item)
            finish1 = time.time()
            delta1 = finish1 - start1
            start2 = time.time()
            index2 = binary_search(sequence, item)
            finish2 = time.time()
            delta2 = finish2 - start2
        except Exception as error:
            print(error)
        finally:
            print(f'{i}: index: {index1}; item: {item}; time: {delta1}')
            print(f'{i}: index: {index2}; item: {item}; time: {delta2}')


if __name__ == '__main__':
    main()
