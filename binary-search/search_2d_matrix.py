# Day 17 - Search a 2D Matrix
# LeetCode #74
# 2D matrix mein target dhundo

def search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        val = matrix[mid // cols][mid % cols]

        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid   1

    return False

# Test
print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))   # True
print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))  # False
print(search_matrix([[1]], 1))                                      # True