# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

# Read the input
input_string, size = input().split()
size = int(size)

# Sort the input string to ensure combinations are in lexicographic order
sorted_string = sorted(input_string)

# Generate combinations for sizes from 1 to the specified size
for i in range(1, size + 1):
    for combo in combinations(sorted_string, i):
        print(''.join(combo))







# Sample Input
# HACK 2

# Sample Output
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK