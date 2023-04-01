# Pre-existing list
numbers = [1, 2, 3]

# Prompt the user to enter a comma-separated list of numbers
input_str = input("Enter a comma-separated list of numbers: ")

# Split the input string into a list of integers
input_list = [int(num) for num in input_str.split(',')]

# Add the input numbers to the pre-existing list
numbers.extend(input_list)

# Print the updated list
print(numbers)
