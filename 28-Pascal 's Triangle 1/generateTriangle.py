from typing import List


def generate(numRows: int) -> List[List[int]]:
    output = [[1]]
    for i in range(1,numRows):
        row = []
        row.append(1)
        for j in range(i-1):
            row.append(output[i-1][j] + output[i-1][j+1]) 
        row.append(1)
        output.append(row)
    return output