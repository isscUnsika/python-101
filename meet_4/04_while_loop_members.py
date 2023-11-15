members = ["Raka", "Delvin", "Azzelya", "Fito"]
print("Current members:")
print(members)

# Dwi is joining the club
members.append("Dwi")

print("Updated members:")
print(members)

n_new_members = int(input("Total new members: "))
i = 0

while i < n_new_members:  # 10 < 10 --> False
    new_member = input("New member: ")
    members.append(new_member)

    i = i + 1

print("Updated members:")

j = 0
while j < len(members):
    print(f"{j+1}. {members[j]}")

    j += 1  # same as `j = j + 1`
