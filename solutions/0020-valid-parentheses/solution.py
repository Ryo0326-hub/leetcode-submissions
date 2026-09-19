class Solution:
    def isValid(self, s: str) -> bool:
        b_dict = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if not stack:
                    return False
                if b_dict[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack
        
