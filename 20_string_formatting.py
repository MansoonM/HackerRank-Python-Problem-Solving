# Given an integer, , print the following values for each integer from to :

# Decimal Octal Hexadecimal (capitalized) Binary Function Description

# Complete the print_formatted function in the editor below.

# print_formatted has the following parameters:

# int number: the maximum value to print Prints

# The four values must be printed on a single line in the order specified above for each from to . Each value should be space-padded to match the width of the binary value of and the values should be separated by a single space.

# Input Format
# A single integer denoting .

# Sample Input
# 17 Sample Output

# Run
# Copy code
# 1     1     1     1
# 2     2     2    10
# 3     3     3    11
# 4     4     4   100
# 5     5     5   101
# 6     6     6   110
# 7     7     7   111
# 8    10     8  1000
# 9    11     9  1001
# 10 12 A 1010 11 13 B 1011 12 14 C 1100 13 15 D 1101 14 16 E 1110 15 17 F 1111 16 20 10 10000 17 21 11 10001

# BLACKBOXAI

# To solve the problem of printing the decimal, octal, hexadecimal, and binary representations of integers from 1 to a given number ( n ), we can follow these steps:

# Input Handling: Read the integer ( n ).
# Determine Width: Calculate the width needed for the binary representation of ( n ) to ensure proper alignment.
# Loop Through Numbers: For each integer from 1 to ( n ):
# Convert the integer to its decimal, octal, hexadecimal (capitalized), and binary forms.
# Print these values, ensuring they are space-padded to match the width of the binary representation.

def print_formatted(number):
    # Calculate the width of the binary representation of the number
    width = len(bin(number)) - 2  # Subtract 2 for the '0b' prefix

    # Loop through each number from 1 to number
    for i in range(1, number + 1):
        # Prepare the formatted output
        decimal = str(i)
        octal = oct(i)[2:]  # Remove '0o' prefix
        hexadecimal = hex(i)[2:].upper()  # Remove '0x' prefix and convert to uppercase
        binary = bin(i)[2:]  # Remove '0b' prefix
        
        # Print the values with the specified formatting
        print(decimal.rjust(width), octal.rjust(width), hexadecimal.rjust(width), binary.rjust(width))

if __name__ == '__main__':
    n = int(input("Enter a number "))
    print_formatted(n)