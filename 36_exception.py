

# Task

# You are given two values  a and b.
# Perform integer division a and b print .

# Input Format

# The first line contains , the number of test cases.
# The next  lines each contain the space separated values of  and .

# Constraints

# Output Format

# Print the value of .
# In the case of ZeroDivisionError or ValueError, print the error code.

# Sample Input
# 3
# 1 0
# 2 $
# 3 1

# Sample Output
# Error Code: integer division or modulo by zero
# Error Code: invalid literal for int() with base 10: '$'
# 3


# Read the number of test cases
n = int(input())

for _ in range(n):
    # Read the input values
    a, b = input().split()
    
    try:
        # Attempt to perform integer division
        result = int(a) // int(b)
        print(result)
    except ZeroDivisionError as e:
        # Handle division by zero
        print("Error Code:", e)
    except ValueError as e:
        # Handle invalid literal for int
        print("Error Code:", e)