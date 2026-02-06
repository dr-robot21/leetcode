def titleToNumber(columnTitle: str) -> int:
    res = 0
    count = len(columnTitle) - 1
    for c in columnTitle:
        res += (ord(c) - ord("A") + 1)*(26**count)
        count -= 1
    return res