from typing import List



def removeDuplicates(nums: List[int]) -> int:
    i = 0 
    j = 0
    n = len(nums)
    if n == 0 : return 0
     
    while i < n:
        if nums[i] != nums[j]:
            j += 1
            nums[i],nums[j] = nums[j],nums[i]
        i += 1
    
    return j + 1


print(removeDuplicates([4]))


