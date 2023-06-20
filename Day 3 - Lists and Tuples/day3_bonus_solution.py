# Day 3 Bonus Challenge: Removing Duplicates from a List (Maintaining Order)

# Allow the user to input a list
user_input = input("Enter a list of comma-separated values: ")
input_list = user_input.split(',')

# Remove duplicates from the list (while maintaining the original order)
no_duplicates_list = []
for element in input_list:
    if element not in no_duplicates_list:
        no_duplicates_list.append(element)

# Output the list without duplicates
print(f"List without duplicates (order maintained): {no_duplicates_list}")
