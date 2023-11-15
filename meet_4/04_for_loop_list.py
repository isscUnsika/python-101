members = ["Raka", "Delvin", "Azzelya", "Fito"]

# print(members[0])
# print(members[3])

# 1: With range()
for i in range(len(members)):  # len stands for 'length'
    print(i+1, end='. ')
    print(members[i])


# 2: With for-each
print(20 * '-')
for item in members:
    print(item)
