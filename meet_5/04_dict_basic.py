"""
dict = {
    key: value,
    key2: value2,
    ...
}
"""


member = {
    "name": "Raka",
    "course": "Python"
}

print(member)

final_test_result = {
    "Linear algebra": 90,
    "Algorithm": 80,
    "Indonesian": 100
}

print(final_test_result)
print(final_test_result["Linear algebra"])

for key in final_test_result:
    print(f"{key}: {final_test_result[key]}")
