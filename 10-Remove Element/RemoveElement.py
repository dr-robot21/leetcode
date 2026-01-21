

from typing import List


def removeElement(self, nums: List[int], val: int) -> int:
    i = 0
    j = 0
    n = len(nums)
    if n == 0 : return 0
    while i < n:
        if nums[i] != val:
            nums[i],nums[j] = nums[j],nums[i]
            j += 1
        i += 1
    return j