from typing import List


def singleNumber( nums: List[int]) -> int:
    single = nums[0]
    for i in range(1,len(nums)):
        single = single ^ nums[i]
    return single