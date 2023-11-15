upper_limit = int(input("Upper limit: "))

for num in range(1, upper_limit + 1):
    if num % 2 == 1:
        print(f"{num} is odd!")
    else:
        print(f"{num} is an even number")
