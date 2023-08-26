def insertion_sort(sorting_list):
    for i in range(1, len(sorting_list)):
        j = i
        temp = sorting_list[i]
        while j > 0 and temp < sorting_list[j - 1]:
            sorting_list[j] = sorting_list[j - 1]
            j -= 1
        sorting_list[j] = temp
    return sorting_list
