import sys


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        prev = i - 1
        while prev >= 0 and arr[prev] > current:
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = current
        print(f'Шаг {i}, отсортировано элементов: {i + 1}, {arr}')


if __name__ == '__main__':
    # n = int(sys.stdin.readline().rstrip())
    # intervals = []
    # for _ in range(n):
    #     l, r = map(
    #         int,
    #         sys.stdin.readline().split()
    #     )
    #     intervals.append((l, r))
    insertion_sort([2, 9, 11, 7, 1])

