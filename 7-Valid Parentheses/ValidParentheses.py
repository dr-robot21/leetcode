
def isValidParentheses(self, s: str) -> bool:
    m = { "{":"}","[":"]","(":")" }
    stack = []
    for item in s:
        if item in "{[(":
            stack.append(m[item])
        elif  len(stack) == 0 or stack.pop() != item:
            return False
    return len(stack) == 0
