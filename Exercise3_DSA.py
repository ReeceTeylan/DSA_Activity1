# Create the process
def print_diamond(n):
    if n % 2 == 0:
        print("Please provide an odd integer.")
        return
    
    for i in range(n):
        stars = '*' * (2 * min(i, n - i - 1) + 1)
        spaces = ' ' * abs(n // 2 - i)
        print(spaces + stars)

# Get user input
n = int(input("Enter an odd integer: "))
print_diamond(n)