

def strStr(haystack: str, needle: str) -> int:
    l = len(needle)
    n = len(haystack)
    for i in range(n - l + 1):
        if haystack[i:i+l] == needle:
            return i
    return -1