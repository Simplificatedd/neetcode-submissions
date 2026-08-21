class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []

        for char in s:
            if char in '({[':
                stack.append(dictionary.get(char))
            elif len(stack) > 0 and char == stack[-1]:
                stack.pop(-1)
            else:
                return False
        if len(stack) > 0:
            return False
        return True