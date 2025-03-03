# easy

# ========================way 1 and the easiest way===========
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
     print(f"Hello {first} {last}! You just delved into python.")
     
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)





# ===>>>>>>>>>>>>>>> way 2 and medium hard to solve

# print frist and last name
def print_full_name(first, last):
    # Create the full name string
    full_name = f"Hello {first} {last}! You just delved into python."
    return full_name  # Return the formatted string

if __name__ == '__main__':
    first_name = input()  # Read the first name from input
    last_name = input()   # Read the last name from input
    result = print_full_name(first_name, last_name)  # Call the function
    print(result)  # Print the result
