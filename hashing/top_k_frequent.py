# Day 11 - Top K Frequent Elements
# LeetCode #347
# K most frequent elements return karo

def top_k_frequent(nums, k):
    count = {}
    freq = [[] for _ in range(len(nums) + 1)]

    for num in nums:
        count[num] = count.get(num, 0) + 1

    for num, cnt in count.items():
        freq[cnt].append(num)

    result = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            result.append(num)
            if len(result) == k:
                return result

    return result

# Test
print(top_k_frequent([1,1,1,2,2,3], 2))  # [1, 2]
print(top_k_frequent([1], 1))             # [1]
print(top_k_frequent([1,2,2,3,3,3], 2))  # [3, 2]