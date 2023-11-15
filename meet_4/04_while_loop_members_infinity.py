members = ["Raka", "Delvin", "Azzelya", "Fito"]
print("Current members:")
print(members)

# Dwi is joining the club
members.append("Dwi")

print("Updated members:")
print(members)

while True:
    new_member = input("New member: ")
    if new_member == 'quit!':
        break

    members.append(new_member)

print("Updated members:")
print(members)
