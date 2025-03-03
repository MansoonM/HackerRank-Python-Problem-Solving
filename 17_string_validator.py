# Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

# str.isalnum()
# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

#  print 'ab123'.isalnum()
# True
#  print 'ab123#'.isalnum()
# False

# print 'abcD'.isalpha()
# True
# print 'abcd1'.isalpha()
# False


if __name__ == '__main__':
    s = input("Enter a String ")

    # Initialize flags for each type
    has_alnum = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False

    # Check each character in the string
    for char in s:
        if char.isalnum():
            has_alnum = True
        if char.isalpha():
            has_alpha = True
        if char.isdigit():
            has_digit = True
        if char.islower():
            has_lower = True
        if char.isupper():
            has_upper = True

    # Print results
    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)