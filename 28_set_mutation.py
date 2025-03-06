# TASK
# You are given a set  and  number of other sets. These  number of sets have to perform some specific mutation operations on set .

# Your task is to execute those operations and print the sum of elements from set .

# Input Format

# The first line contains the number of elements in set .
# The second line contains the space separated list of elements in set .
# The third line contains integer , the number of other sets.
# The next  lines are divided into  parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.

#  len(set(A)) 
#  len(otherSets) 

# Output Format

# Output the sum of elements in set .

# Sample Input

#  16
#  1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
#  4
#  intersection_update 10
#  2 3 5 6 8 9 1 4 7 11
#  update 2
#  55 66
#  symmetric_difference_update 5
#  22 7 35 62 58
#  difference_update 7
#  11 22 35 55 58 62 66
# Sample Output

# 38



# Read the number of elements in the initial set
n = int(input())

# Read the elements of the initial set and convert them to integers
initial_set = set(map(int, input().split()))

# Read the number of operations
m = int(input())

# Execute each operation
for _ in range(m):
    # Read the operation and the length of the other set (length is not used)
    operation_info = input().split()
    operation = operation_info[0]
    length_of_other_set = int(operation_info[1])  # This is read but not used

    # Read the elements of the other set
    other_set = set(map(int, input().split()))

    # Perform the specified operation
    if operation == "intersection_update":
        initial_set.intersection_update(other_set)
    elif operation == "update":
        initial_set.update(other_set)
    elif operation == "symmetric_difference_update":
        initial_set.symmetric_difference_update(other_set)
    elif operation == "difference_update":
        initial_set.difference_update(other_set)

# Print the sum of the elements in the modified set
print(sum(initial_set))