# Task
# Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

# Input Format

# The first line of input contains an integer, .
# The second line contains  space-separated integers.
# The third line contains an integer, .
# The fourth line contains  space-separated integers.

# Output Format

# Output the symmetric difference integers in ascending order, one per line.

# Sample Input
# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}


# Sample Output
# 5
# 9
# 11
# 12

# Read the size of the first set
m = int(input("Enter elements for M: "))
# Read the first set of integers and convert it to a set
a = set(map(int, input().split()))

# Read the size of the second set
n = int(input("Enter elements for N: "))
# Read the second set of integers and convert it to a set
b = set(map(int, input().split()))

# Calculate the symmetric difference
symmetric_difference = a.symmetric_difference(b)

# Sort the result and print each element on a new line
for value in sorted(symmetric_difference):
    print(value)