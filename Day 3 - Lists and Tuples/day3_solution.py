# Day 3 Challenge: Removing Duplicates from a List

# Allow the user to input a list
user_input = input("Enter a list of comma-separated values: ")
input_list = user_input.split(',')

# Remove duplicates from the list
input_set = set(input_list)
no_duplicates_list = list(input_set)

# Output the list without duplicates
print(f"List without duplicates: {no_duplicates_list}")
