# Day 15 - Evaluate Reverse Polish Notation
# LeetCode #150
# Mathematical expression evaluate karo

def eval_rpn(tokens):
    stack = []

    for token in tokens:
        if token in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]

# Test
print(eval_rpn(["2","1","+","3","*"]))         # 9
print(eval_rpn(["4","13","5","/","+"]))         # 6
print(eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 22