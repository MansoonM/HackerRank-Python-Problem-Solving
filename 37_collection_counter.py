# To solve the problem of calculating the total earnings of a shoe shop owner based on customer purchases, we can follow these steps:

# Read the number of shoes and their sizes.
# Read the number of customers and their desired shoe sizes along with the price they are willing to pay.
# For each customer, check if the desired shoe size is available. If it is, add the price to the total earnings and remove that shoe size from the inventory (to prevent multiple sales of the same shoe size).
# Print the total earnings.



# Sample Input

# 10 2 3 4 5 6 8 7 6 5 18 6 6 55 6 45 6 55 4 40 18 60 10 50 Sample Output

# 200 Explanation

# Customer 1: Purchased size 6 shoe for $55. Customer 2: Purchased size 6 shoe for $45. Customer 3: Size 6 no longer available, so no purchase. Customer 4: Purchased size 4 shoe for $40. Customer 5: Purchased size 18 shoe for $60. Customer 6: Size 10 not available, so no purchase.

# Total money earned = //something number


# Read the number of shoes
n = int(input("Number of shoes "))

# Read the shoe sizes and store them in a list
shoe_sizes = list(map(int, input("Size of shoes ").split()))

# Read the number of customers
m = int(input("Number of customers "))

# Create a dictionary to count the available shoes by size
shoe_inventory = {}
for size in shoe_sizes:
    if size in shoe_inventory:
        shoe_inventory[size] += 1
    else:
        shoe_inventory[size] = 1

# Initialize total earnings
total_earnings = 0

# Process each customer
for _ in range(m):
    size, price = map(int, input("Write the Size, Price ").split())
    
    # Check if the desired shoe size is available
    if size in shoe_inventory and shoe_inventory[size] > 0:
        total_earnings += price  # Add the price to total earnings
        shoe_inventory[size] -= 1  # Decrease the inventory for that size

# Print the total earnings
print(total_earnings)