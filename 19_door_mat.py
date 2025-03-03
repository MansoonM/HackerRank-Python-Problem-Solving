# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be X. ( is an odd natural number, and is times .) The design should have 'WELCOME' written in the center. The design pattern should only use |, . and - characters. Sample Designs

# Run
# Copy code
# Size: 7 x 21 
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------

# Size: 11 x 33
# ---------------.|.---------------
# ------------.|..|..|.------------
# ---------.|..|..|..|..|.---------
# ------.|..|..|..|..|..|..|.------
# ---.|..|..|..|..|..|..|..|..|.---
# -------------WELCOME-------------
# ---.|..|..|..|..|..|..|..|..|.---
# ------.|..|..|..|..|..|..|.------
# ---------.|..|..|..|..|.---------
# ------------.|..|..|.------------
# ---------------.|.---------------
# Input Format

# A single line containing the space separated values of and .

# Constraints

# Output Format

# Output the design pattern.

# Sample Input
# 9 27 

# Sample Output
# ------------.|.------------ ---------.|..|..|.--------- ------.|..|..|..|..|.------ ---.|..|..|..|..|..|..|.--- ----------WELCOME---------- ---.|..|..|..|..|..|..|.--- ------.|..|..|..|..|.------ ---------.|..|..|.--------- ------------.|.------------


# Enter your code here. Read input from STDIN. Print output to STDOUT# Read input values
height, width = map(int, input("Enter height and width: ").split())

# Top half of the mat
for i in range(1, height, 2):
    pattern = '.|.' * i
    print(pattern.center(width, '-'))

# Middle of the mat
print('WELCOME'.center(width, '-'))

# Bottom half of the mat
for i in range(height - 2, 0, -2):
    pattern = '.|.' * i
    print(pattern.center(width, '-'))