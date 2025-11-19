def lengthOfLongestSubstring(s : str) -> int :
    hashmap = {}
    l = 0
    rslt = 0
    
    for r in range(len(s)):
        if s[r] in hashmap and hashmap[s[r]] + 1 > l:
            l = hashmap[s[r]] + 1
        hashmap[s[r]] = r
        
        rslt = max(rslt,r - l + 1)
        
    return rslt


print(lengthOfLongestSubstring("abcabcbb"))