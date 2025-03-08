from itertools import permutations

# Read the input
input_string, size = input().split()
size = int(size)

# Generate permutations of the specified size
perm = permutations(sorted(input_string), size)

# Print each permutation in lexicographic order
for p in perm:
    print(''.join(p))





# Sample Input
# HACK 2

# Sample Output
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH
