import operator

# Defining string input to its respective mathematical operations
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


def get_combinations(num1, op1, op2):
    """
    Function to get all the combinations of numbers (0-9)
    which satisfies the equation (n1 op1 n2 op2 n3 = num1)

    :param num1: number which is equal to the equation
    :param op1: First operator of the equation
    :param op2: Second operator of thr equation
    :return: List of combinations of numbers [(n1, n2, n3)...]
    """
    values = []
    # Loops to get 3 numbers which makes a equation using given operator
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if ops[op2](ops[op1](i, j), k) == num1:
                    values.append((i, j, k))
    return values


def get_result(num1, num2, num3, num4, num5, num6):
    """
    Function to get final result of the cross math puzzle
    by using all the combinations of numbers

    :param num1: List of combinations of numbers
    :param num2: List of combinations of numbers
    :param num3: List of combinations of numbers
    :param num4: List of combinations of numbers
    :param num5: List of combinations of numbers
    :param num6: List of combinations of numbers
    :return: List of numbers (0-9) which solves the puzzle in order
    """
    # Loops to compare between the different combinations got for each rows and columns
    values = []
    for n1 in num1:
        a = n1[0]
        b = n1[1]
        c = n1[2]
        for n2 in num2:
            p = n2[0]
            q = n2[1]
            r = n2[2]
            for n3 in num3:
                x = n3[0]
                y = n3[1]
                z = n3[2]
                values = [a, b, c, p, q, r, x, y, z]
                if len(set(values)) == 9:
                    for n4 in num4:
                        if n4[0] == a and n4[1] == p and n4[2] == x:
                            for n5 in num5:
                                if n5[0] == b and n5[1] == q and n5[2] == y:
                                    for n6 in num6:
                                        if n6[0] == c and n6[1] == r and n6[2] == z:
                                            return values
    return values


def print_result(r1, r2, r3, c1, c2, c3):
    """
    Function to print the Final Solution in the readable format

    :param r1: Row 1 data
    :param r2: Row 2 data
    :param r3: Row 3 data
    :param c1: Column 1 data
    :param c2: Column 2 data
    :param c3: Column 3 data
    :return: None
    """
    print("Solution for your cross math puzzle is:")
    print("{:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5}".format(r1[3][0], r1[0], r1[3][1], r1[1], r1[3][2], "=", r1[2]))
    print("{:^5} {:^5} {:^5} {:^5} {:^5}".format(c1[0], " ", c2[0], " ", c3[0]))
    print("{:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5}".format(r2[3][0], r2[0], r2[3][1], r2[1], r2[3][2], "=", r2[2]))
    print("{:^5} {:^5} {:^5} {:^5} {:^5}".format(c1[1], " ", c2[1], " ", c3[1]))
    print("{:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5}".format(r3[3][0], r3[0], r3[3][1], r1[1], r3[3][2], "=", r3[2]))
    print("{:^5} {:^5} {:^5} {:^5} {:^5}".format("=", " ", "=", " ", "="))
    print("{:^5} {:^5} {:^5} {:^5} {:^5}".format(c1[2], " ", c2[2], " ", c3[2]))


def print_input_instructions():
    """
    Function to print the input instructions for the user
    :return: None
    """
    print("Input Instructions:")
    print("Input will be row and column wise operators and its value. For Example:")
    print("{:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5}".format("a", "*", "b", "/", "c", "=", "r1"))
    print("{:^5} {:^5} {:^5} {:^5} {:^5}".format("+", " ", "+", " ", "-"))
    print("{:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5}".format("p", "+", "q", "+", "r", "=", "r2"))
    print("{:^5} {:^5} {:^5} {:^5} {:^5}".format("-", " ", "-", " ", "+"))
    print("{:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5}".format("x", "*", "y", "+", "z", "=", "r3"))
    print("{:^5} {:^5} {:^5} {:^5} {:^5}".format("=", " ", "=", " ", "="))
    print("{:^5} {:^5} {:^5} {:^5} {:^5}".format("c1", " ", "c2", " ", "c3"))
    print("Row 1 input will be: * / r1")
    print("Column 1 input will be: + - c1")
    print("For more info visit https://github.com/BharathN96/Cross-Math/blob/master/README.md", end="\n\n")


def validate_input(list1):
    """
    Function to validate if the input data is a valid or not
    if invalid, the program is terminated
    :param list1: input data as a list
    :return: bool | None
    """
    operands = ("+", "-", "*", "/")
    if len(list1) == 3:
        if list1[0] in operands and list1[1] in operands:
            try:
                int(list1[2])
                return 1
            except ValueError:
                print("Invalid Number input.!! Please check")
                exit()
        else:
            print("Invalid operator input.!! Accepted are +, -, * and /")
            exit()
    else:
        print("Invalid Input format.!! Please check.")
        exit()


# Printing input instructions
print_input_instructions()

# Taking the input from the user row and column wise and storing in a list and validating it
row_1 = list(map(str, input("Enter the Row 1 data: ").split()))
validate_input(row_1)
row_2 = list(map(str, input("Enter the Row 2 data: ").split()))
validate_input(row_2)
row_3 = list(map(str, input("Enter the Row 3 data: ").split()))
validate_input(row_3)
col_1 = list(map(str, input("Enter the Column 1 data: ").split()))
validate_input(col_1)
col_2 = list(map(str, input("Enter the Column 2 data: ").split()))
validate_input(col_2)
col_3 = list(map(str, input("Enter the Column 3 data: ").split()))
validate_input(col_3)

# Getting the combination of the numbers for each row and column
abc_combinations = get_combinations(int(row_1[2]), row_1[0], row_1[1])
pqr_combinations = get_combinations(int(row_2[2]), row_2[0], row_2[1])
xyz_combinations = get_combinations(int(row_3[2]), row_3[0], row_3[1])
apx_combinations = get_combinations(int(col_1[2]), col_1[0], col_1[1])
bqy_combinations = get_combinations(int(col_2[2]), col_2[0], col_2[1])
crz_combinations = get_combinations(int(col_3[2]), col_3[0], col_3[1])

# Finding complexity of Rows and column
rows_complexity = len(abc_combinations) * len(pqr_combinations) * len(xyz_combinations)
column_complexity = len(apx_combinations) * len(bqy_combinations) * len(crz_combinations)

# A flag to check if the solution is valid or not
valid_solution = 0

# Selecting the lowest complex between row and column to reduce the looping time
if rows_complexity <= column_complexity:
    value = get_result(abc_combinations, pqr_combinations, xyz_combinations,
                       apx_combinations, bqy_combinations, crz_combinations)

    # Checking if the solution is a valid one
    if len(set(value)) == 9:
        valid_solution = 1

        # Appending values to its respective rows
        row_1.append((value[0], value[1], value[2]))
        row_2.append((value[3], value[4], value[5]))
        row_3.append((value[6], value[7], value[8]))
else:
    value = get_result(apx_combinations, bqy_combinations, crz_combinations,
                       abc_combinations, pqr_combinations, xyz_combinations)

    # Checking if the solution is a valid one
    if len(set(value)) == 9:
        valid_solution = 1

        # Appending values to its respective rows
        row_1.append((value[0], value[3], value[6]))
        row_2.append((value[1], value[4], value[7]))
        row_3.append((value[2], value[5], value[8]))

# Checking the value of flag
if valid_solution:
    # Printing the solution
    print_result(row_1, row_2, row_3, col_1, col_2, col_3)
else:
    print("No solution exists for this cross math puzzle. Please check input or verify your puzzle")
