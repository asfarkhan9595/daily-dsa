# Day 13 - Valid Parentheses
# LeetCode #20
# Check karo brackets properly closed hain ya  nahi

def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return not stack

# Test
print(is_valid("()"))        # True
print(is_valid("()[]{}"))    # True 
print(is_valid("(]"))        # False
print(is_valid("([)]"))      # False
print(is_valid("{[]}"))      # True  