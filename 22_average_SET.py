#  Input

# STDIN                                       Function
# -----                                       --------
# 10                                          arr[] size N = 10
# 161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]


# output
# 169.375

def average(array):
    # Convert the array to a set to get distinct heights
    distinct_heights = set(array)
    
    # Calculate the average
    avg = sum(distinct_heights) / len(distinct_heights)
    
    # Return the average rounded to 3 decimal places
    return round(avg, 3)

if __name__ == '__main__':
    n = int(input("Enter the size of set/ array: "))
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)