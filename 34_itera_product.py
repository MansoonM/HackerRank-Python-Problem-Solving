# Task

# You are given a two lists  and . Your task is to compute their cartesian product AXB.

# Example

# A = [1, 2]
# B = [3, 4]

# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
# Note:  and  are sorted lists, and the cartesian product's tuples should be output in sorted order.

# Input Format

# The first line contains the space separated elements of list .
# The second line contains the space separated elements of list .

# Both lists have no duplicate integer elements.

# Constraints



# Output Format

# Output the space separated tuples of the cartesian product.

# Sample Input
#  1 2
#  3 4

# Sample Output
#  (1, 3) (1, 4) (2, 3) (2, 4)

# Read input for the first list
A = list(map(int, input().strip().split()))
# Read input for the second list
B = list(map(int, input().strip().split()))

# Compute the Cartesian product using a list comprehension
cartesian_product = [(a, b) for a in A for b in B]

# Print the result in the required format
print(" ".join(str(tup) for tup in cartesian_product))