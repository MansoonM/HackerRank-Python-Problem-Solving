# You are given two sets,  and .
# Your job is to find whether set  is a subset of set .

# If set  is subset of set , print True.
# If set  is not a subset of set , print False.

# Input Format

# The first line will contain the number of test cases, .
# The first line of each test case contains the number of elements in set .
# The second line of each test case contains the space separated elements of set .
# The third line of each test case contains the number of elements in set .
# The fourth line of each test case contains the space separated elements of set .

# Constraints

# Output Format

# Output True or False for each test case on separate lines.

# Sample Input

# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2
# Sample Output

# True 
# False
# False


# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the number of elements in set A
    n = int(input())
    # Read the elements of set A
    set_a = set(map(int, input().split()))
    
    # Read the number of elements in set B
    m = int(input())
    # Read the elements of set B
    set_b = set(map(int, input().split()))
    
    # Check if set A is a subset of set B
    print(set_a.issubset(set_b))