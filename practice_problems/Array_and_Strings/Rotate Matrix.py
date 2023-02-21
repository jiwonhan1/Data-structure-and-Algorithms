# class Solution:
#     def rotate_matrix(self, matrix):
#         # rotates a matrix 90 degrees clockwise
#         n = len(matrix)
#         for layer in range(n//2):
#             first, last = layer, n - layer -1
#             for i in range(first, last):
#                 top = matrix[layer][i]
#
#                 matrix[layer][i] = matrix[matrix-i-1][]