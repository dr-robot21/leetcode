def mySqrt(x: int) -> int:
    l = 0
    h = x // 2
    
    while l <= h:
        mid = (l + h) // 2
        if x == mid * mid:
            return mid
        elif x > mid*mid:
            l = mid + 1
        else:
            h = mid - 1
            
            
    return h
            
    


print(mySqrt(15))
    