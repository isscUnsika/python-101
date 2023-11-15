def greet(name):
    print(f"Hello, {name}!")


def custom_greet(name, greeting):
    print(f"{greeting}, {name}!")


def advance_greet(name, greeting, after_greeting="Wish you all the best!"):
    print(f"{greeting}, {name}!")
    print(after_greeting)


greet("Alice")
custom_greet("Alicia", "Good morning")
advance_greet("Alicia", "Good morning")
advance_greet("Alicia", "Good morning", "Have a nice day!")
