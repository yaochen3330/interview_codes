def check_parentheses_balance(s):
    left_count = 0
    result = []
    marks = [' '] * len(s)  # 默认标记为空格

    # 遍历字符串，处理括号
    for i, char in enumerate(s):
        if char == '(':
            left_count += 1
            result.append(char)
        elif char == ')':
            if left_count > 0:
                left_count -= 1
                result.append(char)
            else:
                marks[i] = '?'
                result.append(char)
        else:
            result.append(char)

    # 处理多余的左括号
    leftover_lefts = left_count
    for i in reversed(range(len(result))):
        if result[i] == '(' and leftover_lefts > 0:
            marks[i] = 'x'
            leftover_lefts -= 1

    return ''.join(result), ''.join(marks)

# 测试用例
test_cases = [
    "bge)))))))))",
    "((IIII)))))",
    "()()()()(uuu",
    "))))UUUU((()"
]

# 处理并输出每个测试用例的结果
for test in test_cases:
    result_str, marks_str = check_parentheses_balance(test)
    print(result_str)
    print(marks_str)
    print()  # 每个测试用例之间添加一个空行
