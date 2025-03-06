# Task

# Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.

# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

# Input Format

# The first line contains the number of students who have subscribed to the English newspaper.
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper.
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

# Constraints


# Output Format

# Output total number of students who have subscriptions to the English or the French newspaper but not both.

# Sample Input

# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output

# 8

# Read the number of students subscribed to the English newspaper
n = int(input())

# Read the roll numbers of students subscribed to the English newspaper
english_subscribers = set(map(int, input().split()))

# Read the number of students subscribed to the French newspaper
m = int(input())

# Read the roll numbers of students subscribed to the French newspaper
french_subscribers = set(map(int, input().split()))

# Find the students who are subscribed to either the English or the French newspaper but not both
only_english_or_french = english_subscribers.symmetric_difference(french_subscribers)

# Print the total number of students who have subscriptions to either newspaper but not both
print(len(only_english_or_french))