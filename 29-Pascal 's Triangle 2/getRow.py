from typing import List


def getRow(self, rowIndex: int) -> List[int]:
    row = [1]
    for i in range(1,rowIndex+1):
        next_el = row[i - 1] * (rowIndex - i + 1) // i
        row.append(next_el)
    return row