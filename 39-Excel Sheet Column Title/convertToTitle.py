def convertToTitle(columnNumber: int) -> str:
    rslt = ''
    while columnNumber > 0:
        columnNumber -= 1
        rslt = chr( columnNumber % 26 + ord("A")) + rslt
        columnNumber //=26
    return rslt 