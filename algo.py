import sys
from typing import Optional, Tuple
from sys import maxsize


def find_two_indexes_quad_O(expected_sum, data):
    for first_index, first_num in enumerate(data):
        for second_index, second_num in enumerate(data):
            if first_index == second_index:
                continue
            elif first_num + second_num == expected_sum:
                return first_index, second_index


def find_two_indexes_linear_O(
        expected_sum: int, data: list[int]
        ) -> Optional[Tuple[int, int]]:
    complements = dict()
    for index, num in enumerate(data):
        complement = expected_sum - num
        if complement in complements and complements[complement] != index:
            return complements[complement], index
        complements[num] = index


def two_pointer_method(
        expected_sum: int, data: list[int]
        ) -> Optional[Tuple[int, int]]:
    left_pointer = 0
    right_pointer = len(data) - 1
    while left_pointer < right_pointer:
        result = data[left_pointer] + data[right_pointer]
        if result == expected_sum:
            return (left_pointer, right_pointer)
        elif result > expected_sum:
            right_pointer -= 1
        else:
            left_pointer += 1



def find_min_slice_sum(data, elements_in_slice):
    # Считаем сумму первого окна.
    window_sum = sum(data[0:elements_in_slice])
    print(data[0:elements_in_slice])
    # Запоминаем результат подсчёта в качестве минимальной суммы.
    min_sum = window_sum
    # В цикле перебираем индексы массива от elements_in_slice до последнего.
    for index in range(elements_in_slice, len(data)):
        # К сумме предыдущего окна добавляем новый элемент
        # и вычитаем "вышедший":
        window_sum += data[index] - data[index - elements_in_slice]
        # Находим минимальную сумму.
        min_sum = min(min_sum, window_sum)
    return min_sum


if __name__ == '__main__':
    data = [5, -3, -2, 10, 2, 7, 1, -6, 13]
    elements_in_slice = 4
    print(find_min_slice_sum(data, elements_in_slice))
