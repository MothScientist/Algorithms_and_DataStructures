def binary_search(nums: list[int], target: int) -> bool:
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        middle = (high + low) // 2
        middle_val = nums[middle]
        if middle_val == target:
            return True
        elif middle_val > target:
            high = middle - 1
        else:
            low = middle + 1

    return False
