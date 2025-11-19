def twoSum(arr : list , target : int) -> list :
    output = [-1,-1]
    hashmap = {}
    
    for i,item in enumerate(arr) :
        print(item)
        x = target - item
        if x in hashmap:
            return [i,hashmap[x]]
        hashmap[item] = i
        
    return []
    

print(twoSum([7,2,11,13],18))