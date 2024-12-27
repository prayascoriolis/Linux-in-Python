'''13. Write a program to parse and evaluate mathematical expressions (e.g., 2 + 3 * 5, 22/7=3.14).'''

def evaluate_expression(expr):
    def calculate(operators, values):
        # Perform the calculation for the last operator and its operands
        right = values.pop()
        left = values.pop()
        op = operators.pop()
        if op == '+':
            values.append(left + right)
        elif op == '-':
            values.append(left - right)
        elif op == '*':
            values.append(left * right)
        elif op == '/':
            values.append(left / right)

    def precedence(op):
        # Define precedence for operators
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    # Stacks to store operators and values
    operators = []
    values = []

    i = 0
    while i < len(expr):
        char = expr[i]

        if char == ' ':
            i += 1
            continue
        # Parse int and float
        if char.isdigit() or char == '.':
            num = []
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                num.append(expr[i])
                i += 1
            values.append(float(''.join(num)))
            continue

        if char in ('+', '-', '*', '/'):
            while (operators and precedence(operators[-1]) >= precedence(char)):
                calculate(operators, values)
            operators.append(char)
        i += 1

    while operators:
        calculate(operators, values)

    return values[0]

expression = "2 + 3 * 5"
print(f"Result: {evaluate_expression(expression)}")  # Output: 17

expression = "22 / 7"
print(f"Result: {evaluate_expression(expression)}")  # Output: 3.142857142857143
