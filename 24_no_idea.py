# Input Format

# The first line contains integers  and  separated by a space.
# The second line contains  integers, the elements of the array.
# The third and fourth lines contain  integers,  and , respectively.

# Output Format

# Output a single integer, your total happiness.

# Sample Input

# 3 2
# 1 5 3
# 3 1
# 5 7
# Sample Output

# 1
# Explanation

# You gain  unit of happiness for elements  and  in set . You lose  unit for  in set . The element  in set  does not exist in the array so it is not included in the calculation.
# Read the first line of input
n, m = map(int, input("Enter two number ").split())

# Read the array of integers
array = list(map(int, input("Enter the numbers ").split()))

# Read the integers in set A
set_a = set(map(int, input("Enter the numbers ").split()))

# Read the integers in set B
set_b = set(map(int, input("Enter the number ").split()))

# Initialize happiness
happiness = 0

# Calculate happiness based on the array
for number in array:
    if number in set_a:
        happiness += 1  # Gain happiness
    elif number in set_b:
        happiness -= 1  # Lose happiness

# Output the final happiness
print(happiness)