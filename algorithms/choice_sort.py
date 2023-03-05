import time
import random


# В этом варианте много перестановок: не запоминается индекс текущего
# мин.значения, а сразу меняется местами.

def choice_sort_var1(arr):
    """Сортирует по возрастанию. Изменяет исходный список"""
    N = len(arr)
    for pos in range(N-1):
        for k in range(pos+1, N):
            if arr[k] < arr[pos]:
                arr[k], arr[pos] = arr[pos], arr[k]
    return arr


# В этом варианте тоже двойной цикл, но перестановка только одна - после
# вложенного цикла, когда найден текущий минимум.

def choice_sort_var2(arr):
    """Сортирует по возрастанию. Изменяет исходный список"""
    N = len(arr)
    for pos in range(N-1):
        cur_min = pos
        for k in range(pos+1, N):
            if arr[k] < arr[pos]:
                cur_min = k
        arr[pos], arr[cur_min] = arr[cur_min], arr[pos]
    return arr


# Пример из книжки:
# Двойной цикл разбит на 2 функции: поиск мин и добавление мин в новый массив

def find_smallest(arr):
    """Ищет минимум в списке. Возвращает индекс минимума"""
    smallest = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            index = i
    return index


def choice_sort_var3(arr):
    """Сортирует по возрастанию. Возвращает новый список."""
    new_arr = []
    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


data = [
    (1, [random.randint(1, 50) for _ in range(10)]),
    (2, [random.randint(1, 1000) for _ in range(100)]),
    (3, [random.randint(1, 10000) for _ in range(1000)]),
    (4, [random.randint(1, 100000) for _ in range(10000)]),
    (5, [random.randint(1, 1000000) for _ in range(100000)])
]


def main():
    for i, arr in data:
        try:
            start1 = time.time()
            choice_sort_var2(arr)
            finish1 = time.time()
            start2 = time.time()
            choice_sort_var1(arr)
            finish2 = time.time()
            start3 = time.time()
            choice_sort_var3(arr)
            finish3 = time.time()
        except Exception as error:
            print(error)
        finally:
            print(f'{i}: {choice_sort_var2.__name__}, time:{finish1 - start1}')
            print(f'{i}: {choice_sort_var1.__name__}, time:{finish2 - start2}')
            print(f'{i}: {choice_sort_var3.__name__}, time:{finish3 - start3}')


if __name__ == '__main__':
    main()
