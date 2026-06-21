# Day 10 - Group Anagrams
# LeetCode #49
# Same characters wale strings ko group karo

def group_anagrams(strs):
    anagram_map = {}

    for word in strs:
        key = tuple(sorted(word))
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(word)

    return list(anagram_map.values())

# Test
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# [['eat','tea','ate'], ['tan','nat'], ['bat']]

print(group_anagrams([""]))
# [['']]

print(group_anagrams(["a"]))
# [['a']]