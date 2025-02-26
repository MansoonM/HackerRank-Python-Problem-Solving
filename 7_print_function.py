#easy

# The included code stub will read an integer, n, from STDIN.

# Without using any string methods, try to print the following:
# 1,2,3,4....n

# Note that "..." represents the consecutive values in between.

# Example: i/p: n=5 ,  o/p:   1 2 3 4 5

number= int(input("Enter a number "))

result=''.join(str(i) for i in range(1, number+1))

print("Result ", result)
