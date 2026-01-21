from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    l = 0
    h = len(nums) - 1
    mid = 0
    
    if nums[h] < target:
        return h + 1
    
    while l <= h:
        mid = (l + h) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            h = mid - 1
    
    return l
    
            

print(searchInsert([1,5,9,13],3))