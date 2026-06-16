# Day 5 - Valid Palindrome
# LeetCode #125
# String palindrome hai agar reverse same ho

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

# Test
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                       # False
print(is_palindrome(" "))                                # True