def climbStairs(n: int) -> int:
    if n <= 3 : return n
        
    u ,v = 2,3
    count = 0
    for _  in range(3,n):
        count = u + v
        u = v
        v = count
        
    return count