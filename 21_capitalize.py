#easy 

# Input Format

# A single line of input containing the full name, .

# The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

# Output Format

# Print the capitalized string, .

# Sample Input

# chris alan
# Sample Output

# Chris Alan

import os

# Complete the solve function below.
def solve(s):
    # Split the input string into words while preserving spaces
    words = s.split(' ')  # Split by space to preserve multiple spaces
    
    # Capitalize each word and join them back into a single string
    capitalized_words = [word.capitalize() for word in words]
    result = ' '.join(capitalized_words)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
