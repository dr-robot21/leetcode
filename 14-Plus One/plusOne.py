from typing import List


def plusOne(digits: List[int]) -> List[int]:

    carry = 1
    i = len(digits) - 1
    while i >= 0 :
        tmp = digits[i]
        digits[i] = (carry + digits[i]) % 10
        carry = (tmp + carry) // 10
        i -= 1
    if carry != 0:
        digits.insert(0,carry)
    return digits