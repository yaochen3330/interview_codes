def check_parentheses_balance(s):
    balance = 0
    result = []
    marks = [' '] * len(s)

    for i, char in enumerate(s):
        if char == '(':
            balance += 1
            result.append(char)
        elif char == ')':
            if balance > 0:
                balance -= 1
                result.append(char)
            else:
                marks[i] = '?'
                result.append(char)
        else:
            result.append(char)

    # Handle any unmatched '('
    for i in reversed(range(len(result))):
        if result[i] == '(' and balance > 0:
            marks[i] = 'x'
            balance -= 1

    return ''.join(result), ''.join(marks)
