members = ["Raka", "Delvin", "Azzelya", "Fito"]
print("Current members:")
print(members)

# Dwi is joining the club
members.append("Dwi")

print("Updated members:")
print(members)

n_new_members = int(input("Total new members: "))

for i in range(n_new_members):
    new_member = input("New member: ")
    members.append(new_member)

print("Updated members:")
print(members)
