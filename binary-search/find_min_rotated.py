# Day 18 - Find Minimum in Rotated Sorted Array
# LeetCode #153

def find_min(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

# Test
print(find_min([3,4,5,1,2]))      # 1
print(find_min([4,5,6,7,0,1,2]))  # 0
print(find_min([11,13,15,17]))    # 11 