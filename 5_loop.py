#easy

# The provided code stub reads an integer, n,  from STDIN. For all non-negative integers i<n, print i^2 .

# n=3 op=0 1 4 ,        n =3 so [0,1,2]

num= int(input("Enter a number "))
# num = 2 
for i in range(num):   # i= num[0,1]    #range always starts from zero
    print(i*i)


    # num range =0,1,2,3,4 (num-1)
    #  0 1 4 9 16