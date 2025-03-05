# Task

# Apply your knowledge of the .add() operation to help your friend Rupal.

# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.

# Find the total number of distinct country stamps.

# Input Format

# The first line contains an integer , the total number of country stamps.
# The next  lines contains the name of the country where the stamp is from.

# Constraints


# Output Format

# Output the total number of distinct country stamps on a single line.

# Sample Input
# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France 

# Sample Output
# 5

# Explanation
# UK and France repeat twice. Hence, the total number of distinct country stamps is  (five).

# Read the total number of country stamps
n = int(input())

# Initialize an empty set to store distinct country names
country_stamps = set()

# Read each country name and add it to the set
for _ in range(n):
    country = input().strip()  # Read the country name and remove any extra whitespace
    country_stamps.add(country)  # Add the country name to the set

# Output the total number of distinct country stamps
print(len(country_stamps))