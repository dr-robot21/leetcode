from typing import List

def missingRanges(nums : List[int] , lower : int , upper : int ) -> List[List[int]] :
    
    n = len(nums)
    if n == 0 : return [[lower,upper]]
    
    output = []
    
    if nums[0] > lower:
        output.append([lower , nums[0] - 1])
    
    for i in range(n - 1):
        if nums[i + 1] - nums[i] > 1:
            output.append([nums[i] + 1 , nums[i + 1] - 1])
    
    if nums[n - 1] < upper: 
        output.append([nums[n-1] + 1 , upper])
        
    return output



    