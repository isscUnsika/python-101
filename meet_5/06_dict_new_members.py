members = [
    {
        "name": "Raka",
        "course": "Python"
    },
    {
        "name": "Delvin",
        "course": "UI/UX"
    },
    {
        "name": "Azzelya",
        "course": "Web Development"
    },
    {
        "name": "Fito",
        "course": "Data Engineering"
    }
]

print("Current members:")
print(members)

while True:
    new_member = dict()
    new_member["name"] = input("New member name: ")

    if new_member["name"] == 'quit!':
        break

    new_member["course"] = input("New member course: ")
    members.append(new_member)

print("Updated members:")
print(members)
