from typing import List


def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 0 : return ""

    prefix = strs[0]
    length = len(prefix)

    for s in strs:
        while not s.startswith(prefix[:length]):
            length -= 1
            if length == 0:
                return ""
    return prefix[:length]
    
print(longestCommonPrefix(["flower","flow","flight"]))