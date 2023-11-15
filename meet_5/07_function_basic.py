def greet(name, course="Python"):
    print(f"Hello, {name}!", end=" ")
    print(f"How is your {course} today?")

    return f"{name} -- {course}"


def count_even_number(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1

    return count


# delvin = greet("Delvin", "Python")
# farhan = greet("Farhan", "UI/UX")
hanif = greet("Hanif")

print(hanif)


my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_number = count_even_number(my_numbers)

print(even_number)

my_numbers_2 = [10, 11, 12, 13, 14, 15, 16, 17, 18]
even_number = count_even_number(my_numbers_2)
print(even_number)
