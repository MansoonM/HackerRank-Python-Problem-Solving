# You are given a set  and  other sets.
# Your job is to find whether set  is a strict superset of each of the  sets.

# Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.

# Example
# Set is a strict superset of set.
# Set is not a strict superset of set.
# Set is not a strict superset of set.

# Input Format

# The first line contains the space separated elements of set .
# The second line contains integer , the number of other sets.
# The next  lines contains the space separated elements of the other sets.

# Constraints

# Output Format

# Print True if set  is a strict superset of all other  sets. Otherwise, print False.

# Sample Input 0

# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12
# Sample Output 0

# False
# Explanation 0

# Set  is the strict superset of the set but not of the set because  is not in set .
# Hence, the output is False.




# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the elements of set A and convert them to a set
set_a = set(map(int, input().split()))

# Read the number of other sets
n = int(input())

# Initialize a flag to True
is_strict_superset = True

# Process each of the other sets
for _ in range(n):
    # Read the elements of the other set and convert them to a set
    other_set = set(map(int, input().split()))
    
    # Check if set A is a strict superset of the other set
    if not (set_a > other_set):  # > operator checks for strict superset
        is_strict_superset = False
        break  # No need to check further if one fails

# Print the result
print(is_strict_superset)