# Day 9 - Minimum Size Subarray Sum
# LeetCode #209
# Minimum length subarray   dhundo jiska sum >= target ho

def min_subarray_len(target, nums):
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len

# Test
print(min_subarray_len(7, [2,3,1,2,4,3]))  # 2
print(min_subarray_len(4, [1,4,4]))         # 1
print(min_subarray_len(11, [1,1,1,1,1]))    # 0