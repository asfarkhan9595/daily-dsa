# Day 3 - Valid Anagram
# LeetCode #242
# Two strings anagram hain agar same characters same count mein hon

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        count[char] = count.get(char, 0) - 1
        if count[char] < 0:
            return False
    return True

# Test
print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False
print(is_anagram("listen", "silent"))    # True