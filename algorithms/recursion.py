# Ex. 4.1 function sum
def total(arr):
    if len(arr) == 1:
        return arr[0]
    ans = arr[0] + sum(arr[1:])
    return ans


# Ex. 4.2 count element
def count(arr):
    if len(arr) == 1:
        return 1
    ans = 1 + count(arr[1:])
    return ans


# Ex. 4.3 max element
def maximum(arr):
    if len(arr) == 1:
        return arr[0]
    head = arr[0]
    tail = arr[1:]
    if head > maximum(tail):
        return head
    return maximum(tail)


data = [
    [2, 3, 8, 1, 10, 3],
    [1],
    [10, 9, 4, 1, 0, 3],
    [3, 5, 1, 3, 9, 15]
]

if __name__ == '__main__':
    for arr in data:
        print(total(arr))
        print(count(arr))
        print(maximum(arr))
