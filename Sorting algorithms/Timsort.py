def _insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        key_item = array[i]
        j = i - 1
        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array


def _merge(left_array, right_array):
    if not left_array:
        return right_array
    elif not right_array:
        return left_array
    elif left_array[0] < right_array[0]:
        return [left_array[0]] + _merge(left_array[1:], right_array)
    else:
        return [right_array[0]] + _merge(left_array, right_array[1:])


def timsort(array):
    min_run = 32
    n = len(array)

    for i in range(0, n, min_run):
        array = _insertion_sort(array, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid_point = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))

            merged_array = _merge(
                array[start: mid_point + 1],
                array[mid_point + 1: end + 1],
            )

            array[start: start + len(merged_array)] = merged_array

        size *= 2

    return array
