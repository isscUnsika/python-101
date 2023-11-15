members = ["Raka", "Delvin", "Azzelya", "Fito"]
print("Current members:")
print(members)


courses = ["Python", "UI/UX", "Web Development", "Data Engineering"]
print("Current courses:")
print(courses)

print()
for member, course in zip(members, courses):
    print(f"{member} is taking {course}")


# Add new member and course
members.append("Frieren")
# courses.append("Data Science")

print()
print("Updated members:")
for member, course in zip(members, courses):
    print(f"{member}: {course}")

print(members)
