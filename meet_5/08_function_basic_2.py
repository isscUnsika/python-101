def add_numbers(num1, num2):
    return num1 + num2


result = add_numbers(5, 7)
print(result)  # Output: 12


def count_even_numbers(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1

    return count


my_numbers = [1, 11, 13, 15, 17, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 0]
result = count_even_numbers(my_numbers)
print(result)  # Output: 5
