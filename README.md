# Cross-Math
Cross Math is a python script which gives a solution for a [cross math puzzle](https://www.pleacher.com/mp/puzzles/mathpuz/mobcm39.html)

## Cross Math Puzzle
Cross math puzzle is a mathematical puzzle which plays around with numbers and basic mathematical operations +, -, * and /

Its goal is to find numbers from 1 to 9 which solves the given equations

For example:

![image](https://github.com/BharathN96/Cross-Math/blob/example_image/images/example_image.png)

We must fill the missing blocks with 1 to 9 without repetitions such that each row and column sums up to value mentions at the end of its respective row or column.

## Pre-Requisite
[Python](https://www.python.org/) version 3.7+

## Execution of the program
Open python terminal/console and run the command
```bash
python cross_math.py
```
Provide your puzzle in the required input format and output will be solution for your problem

## Input instructions
Input will be a row and column-wise operators and its value with space-separated in between them.
For Example
```bash
 a   *   b   /   c   =  r1 
 +       +       - 
 p   +   q   +   r   =  r2 
 -       -       + 
 x   *   y   +   z   =  r3 
 =       =       = 
c1      c2      c3 
```
Row 1 input will be: (operator1 operator2 value_of_the_row)
```bash
* / r1
```
Column 1 input will be: (operator1 operator2 value_of_the_column)
```bash
+ - c1
```

## Output
Program output will be solution for the cross math puzzle

## Sample input and output
Problem:

![image](https://github.com/BharathN96/Cross-Math/blob/example_image/images/example_image.png)

Input:
```bash
Enter the Row 1 data: * / 12
Enter the Row 2 data: + + 15
Enter the Row 3 data: * + 16
Enter the Column 1 data: + - 1
Enter the Column 2 data: + - 13
Enter the Column 3 data: - + 7
```
Output:
```bash
Solution for your cross math puzzle is:
 3   *   8   /   2   =  12 
 +       +       - 
 5   +   6   +   4   =  15 
 -       -       + 
 7   *   1   /   9   =  16 
 =       =       = 
 1      13       7 
 ```
