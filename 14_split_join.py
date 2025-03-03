#easy

# first spilt--------------------->>>...
#  a = "this is a string"
#  a = a.split(" ") # a is converted to a list of strings. 
#  print a
# ['this', 'is', 'a', 'string']

# Secondly joint--------------------->>>...
#  a = "-".join(a)
#  print a
# this-is-a-string 


def split_and_join(line):
    # Split the line into words
    words = line.split()  # This splits the string by whitespace
    # Join the words with a hyphen
    joined_line = "-".join(words)  # This joins the words with a hyphen
    return joined_line  # Return the joined string



if __name__ == '__main__':
    line = input()  # Read input from the user
    result = split_and_join(line)  # Call the function
    print(result)  # Print the result