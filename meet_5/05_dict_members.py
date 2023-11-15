members = [
    {
        "name": "Raka",
        "course": "Python",
        "age": 20,
    },
    {
        "name": "Delvin",
        "course": "UI/UX",
        "height": 170,
    },
    {
        "name": "Azzelya",
        "course": "Web Development",
    },
    {
        "name": "Fito",
        "course": "Data Engineering",
        "ages": 20.0
    }
]

print("Current members:")
print(members)

# print("\nFirst member:")
# print(members[-1])
# print(members[-1]["name"])
# print(members[-1]["course"])

# print("\nAll members:")
# for member in members:
#     print(f"{member['name']} is taking {member['course']}")


# Add new member
new_member = {
    "name": "Frieren",
    "course": "Data Science",
}

members.append(new_member)

print("\nUpdated members:")
for member in members:
    print(f"{member['name']}: {member['course']}")

new_members = [
    {
        "name": "Farhan",
        "course": "Python",
    },
    {
        "name": "Hanif",
        "course": "Python",
    }
]

members += new_members

print("\nLatest members:")
for member in members:
    if member["course"] == "Python":
        print(f"{member['name']} is taking {member['course']}")
