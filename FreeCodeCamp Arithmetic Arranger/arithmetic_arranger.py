def arithmetic_arranger(problems, result=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ''
    first_line = ''
    second_line = ''
    dashes_line = ''
    results_line = ''
    space = ' ' * 4

    for problem in problems:
        operand_1, operator, operand_2 = problem.split()
        if operator == "/" or operator == "*":
            return "Error: Operator must be '+' or '-'."
        elif not operand_1.isdigit() or not operand_2.isdigit():
            return "Error: Numbers must only contain digits."
        elif len(operand_1) > 4 or len(operand_2) > 4:
            return "Error: Numbers cannot be more than four digits."
        # first line = first operands + spaces
        if len(operand_1) > len(operand_2):
            longest = operand_1
        else:
            longest = operand_2
        dashes = '-' * (len(longest) + 2)
        space_operand_1 = ' ' * ((len(longest) + 2) - len(operand_1))

        # first line
        first_line += space_operand_1 + operand_1 + space


        # second line
        space_operand_2 = ' ' * ((len(longest)) - len(operand_2))
        second_line += operator + ' ' + space_operand_2 + operand_2 + space

        # dashes line
        dashes_line += dashes + space

        # Calculate operations result
        operand_1_num = int(operand_1)
        operand_2_num = int(operand_2)

        if operator == '+':
            operation_res = operand_1_num + operand_2_num
            space_result = ' ' * ((len(longest) + 2) - len(str(operation_res)))
            # result line
            results_line += space_result + str(operation_res) + space
        elif operator == '-':
            operation_res = operand_1_num - operand_2_num
            # result line
            space_result = ' ' * ((len(longest) + 2) - len(str(operation_res)))
            results_line += space_result + str(operation_res) + space

    # putting it all together
    if result:
        arranged_problems += first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashes_line.rstrip() + '\n' + results_line.rstrip()
    else:
        arranged_problems += first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashes_line.rstrip()
    # print(len(arranged_problems))
    return arranged_problems


# print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))
