def heapify(nums, heap_size, root_index):
    # The index of the largest element is considered the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index and the element is greater than
    # than the current largest, update the largest elementт
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # Same for the right child of the root
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # If the largest element is no longer the root, they are swapped
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    # Create Max Heap from list
    # The second argument means to stop the algorithm before the element -1, i.e.
    # before the first element of the list
    # The 3rd argument means iterate through the list in the opposite direction,
    # decrement counter i by 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Move the Max Heap Root to the End of the List
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)