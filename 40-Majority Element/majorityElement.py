from typing import List


def majorityElement(nums: List[int]) -> int:
    
    majority = res = 0
    for n in nums:
        if majority == 0:
            res = n
        
        majority += 1 if n == res else -1
    return res