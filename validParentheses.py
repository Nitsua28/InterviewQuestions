'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

'''
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if len(stack) > 0:
                    pop = stack.pop()
                    if (pop == "(" and i != ")") or (pop == "{" and i != "}") or (pop == "[" and i != "]"):
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
