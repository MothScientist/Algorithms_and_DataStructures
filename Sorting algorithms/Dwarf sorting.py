def dwarf_sort_0(arr):
    i, size = 1, len(arr)
    while i < size:
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1
    return arr


def dwarf_sort_1(arr):
    i, j, size = 1, 2, len(arr)
    while i < size:
        if arr[i - 1] <= arr[i]:
            i, j = j, j + 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return arr
