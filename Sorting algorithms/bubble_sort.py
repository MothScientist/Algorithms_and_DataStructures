def bubble_sort(sorting_list):
    l = len(sorting_list)
    for i in range(l):
        for j in range(0, l - i - 1):
            if sorting_list[j] > sorting_list[j + 1]:
                sorting_list[j], sorting_list[j + 1] = sorting_list[j + 1], sorting_list[j]

    return sorting_list
