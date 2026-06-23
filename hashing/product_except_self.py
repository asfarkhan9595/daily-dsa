# Day 12 - Product of Array Except Self
# LeetCode #238
# Har element ke liye baaki sab ka product return karo
# Division use nahi karna!

def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Left prefix product
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Right suffix product
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

# Test
print(product_except_self([1, 2, 3, 4]))   # [24, 12, 8, 6]
print(product_except_self([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]