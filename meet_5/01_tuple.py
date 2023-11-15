# List, it is a 'mutable' data type

img_dimension = [1920, 1080, 3]
print(f"Initial dimension: {img_dimension}")
print(f"First element: {img_dimension[0]}")

img_dimension[0] = 1080
print(f"Changed dimension: {img_dimension}")

img_dimension.append(30.5)
print(f"Added dimension: {img_dimension}")


# Tuple, it is an 'immutable' data type

img_dimension_tuple = (1920, 1080, 3)
print(f"Initial tuple dimension: {img_dimension_tuple}")
print(f"First element: {img_dimension_tuple[0]}")

# img_dimension_tuple[0] = 1080
# print(f"Changed dimension: {img_dimension_tuple}")

img_dimension_tuple.append(30.5)
