def print_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    print("Output:", positive_numbers)

# Input: list1 = [12, -7, 5, 64, -14]
list1 = [12, -7, 5, 64, -14]
print("Input:", list1)
print_positive_numbers(list1)

# Input: list2 = [12, 14, -95, 3]
list2 = [12, 14, -95, 3]
print("Input:", list2)
print_positive_numbers(list2)
