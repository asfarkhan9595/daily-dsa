# Day 14 - Min Stack
# LeetCode #155
# Stack jo minimum element O(1) mein return kare

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]

# Test
stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.get_min())  # -3
stack.pop()
print(stack.top())      # 0
print(stack.get_min())  # -2