from vector import Vector

# v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
# v2 = v1 * 5
# print(v2)

# v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
# v2 = v1 * 5
# print(v2)

# v2 = v1 / 2.0
# print(v2)

# v1 / 0.0

# 2.0 / v1

# print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)

# print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)

# print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)

# v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
# print(v1.shape)


# v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
# print(v1)
# print(v1.shape)
# # Expected output:
# (4,1)
# print(v1.T())
# # Expected output:
# # Vector([[0.0, 1.0, 2.0, 3.0]])
# print(v1.T().shape)
# # Expected output:
# # (1,4)
# # Example 2:
# v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
# print(v2.shape)
# # Expected output:
# # (1,4)
# print(v2.T())
# # Expected output:
# # Vector([[0.0], [1.0], [2.0], [3.0]])
# print(v2.T().shape)
# # Expected output:
# # (4,1)


v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
print(v1.dot(v2))
# Expected output:
# 18.0
v3 = Vector([[1.0, 3.0]])
v4 = Vector([[2.0, 4.0]])
print(v3.dot(v4))
# Expected output:
# 14.0
v1
# Expected output: to see what __repr__() should do
# [[0.0, 1.0, 2.0, 3.0]]
print(v1)
# Expected output: to see 