def double_elements(numbers):
    # Create a new list with each element doubled
    doubled_numbers = [num * 2 for num in numbers]
    return doubled_numbers

# Example usage
numbers = [1, 2, 3, 4]
doubled_numbers = double_elements(numbers)

print("Original list:", numbers)
print("Doubled list:", doubled_numbers)
