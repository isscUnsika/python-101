"""
dict = {
    key: value,
    key2: value2,
    ...
}
"""


member = {
    "name": "Raka",
    "course": "Python",
    "age": 19,
}

print(member)
print(member["name"])


primary_member = {
    "Raka": {
        "name": "Raka",
        "course": "Python",
        "age": 19,
    }
}

print()
print(primary_member["Raka"])

primary_member["Raka"]["age"] += 1
primary_member["Raka"]["course"] = "UI/UX"
primary_member["Raka"]["height"] = 170.22
primary_member["Raka"]["height"] = 170.50

print(primary_member["Raka"])


# final_test_result = {
#     "Linear algebra": 90,
#     "Algorithm": 80,
#     "Indonesian": 100
# }

# print(final_test_result)
# print(final_test_result["Linear algebra"])
# print(final_test_result["Algorithm"])


# for test_res in final_test_result:
#     print(f"{test_res}: {final_test_result[test_res]}")
