upper_limit = int(input("Upper limit: "))

number = 1

while number <= upper_limit:
    if number % 2 == 1:
        print(f"{number} is odd!")
    else:
        print(f"{number} is an even number")

    number = number + 1
