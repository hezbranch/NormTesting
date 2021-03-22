## Hezekiah Branch
## Purpose: Provides simulation of 2-Norm and explores vector-matrix transposition
## Inspired by content from MATH 126: Numerical Linear Algebra
## Tufts University, Spring 2021

import math
import random

def dot_product(vector_X, vector_Y, dimension):
    if len(vector_X) != len(vector_Y):
        raise Exception("Matrix error! Dimensions must agree.)")
    dot_product = 0
    for idx in range(dimension):
        dot_product += vector_X[idx] * vector_Y[idx]
    return dot_product

def cos_theta(vector_X, vector_Y, dimension):
    if len(vector_X) != len(vector_Y):
        raise Exception("Matrix error! Dimensions must agree.)")
    numerator = dot_product(vector_X, vector_Y, dimension)
    x_norm = math.sqrt(dot_product(vector_X, vector_X, dimension))
    y_norm = math.sqrt(dot_product(vector_Y, vector_Y, dimension))
    denominator = x_norm * y_norm
    cos_theta = numerator / denominator
    return {"cos_theta":cos_theta, "x_norm":x_norm, "y_norm":y_norm}

def L2_norm(vector):
    return math.sqrt(dot_product(vector, vector, len(vector)))

def vector_add(u, v):
    if len(u) != len(v):
        raise Exception("Matrix error! Dimensions must agree.)") 
    return [u[i] + v[i] for i in range(len(u))]

def vector_subtract(u, v):
    if len(u) != len(v):
        raise Exception("Matrix error! Dimensions must agree.)") 
    return [u[i] - v[i] for i in range(len(u))]

def row_vect_to_column_vect(u):
    return [[row] for row in u]

def column_vect_to_row_vect(u):
    return [row[0] for row in u]

def vec_transpose(u):
    if type(u[0]) == int or type(u[0]) == float or type(u[0]) == complex:
        return row_vect_to_column_vect(u)
    else:
        return column_vect_to_row_vect(u)

def matrix_transpose(A):
    if len(A) != len(A[0]):
        raise Exception("Dimension error! N x N matrices only.)")
    for i in range(len(A)):
        for j in range(len(A)):
            if i > j:
                temp = A[i][j]
                A[i][j] = A[j][i]
                A[j][i] = temp
    return A

def error_check(solution):
    print("Error check only used for distance to 30 deg!!!")
    return abs(0.86602540378 - solution)


## Modify values below to test different approx of cos theta
## which should approach 30 deg as dimension approaches infinity
## Test increasing levels of dimensionality to explore claim
'''
dimensionalities = [4, 14, 20, 24, 30, 34, 40, 
45, 50, 100, 200, 300, 500, 800, 2000, 30000, 500000, 1000000]
for dimension in dimensionalities:
    vector_X = [1 for i in range(1, dimension + 1)]
    vector_Y = [i for i in range(1, dimension + 1)]
    solution = cos_theta(vector_X, vector_Y, dimension)
    print("Dimensionality: ", dimension)
    print("cos_theta: ", solution["cos_theta"])
    print("Amount of error from 30 deg: ", error_check(solution["cos_theta"]))
    print("-------------------------------------------------\n\n")
'''
# Evidence in support of the Triangle Inequality
x = [1, 8, 5, -2]
y = [5, 3, 4, 7]

x_plus_y = vector_add(x, y)
x_plus_y_norm = L2_norm(x_plus_y)
x_norm = L2_norm(x)
y_norm = L2_norm(y)


print("Investigating the Triangle Inequality...\n")
print("By def., [X + Y] L2 norm <= X L2 norm + Y L2 norm\n")
print("[X + Y] norm gives us: ", x_plus_y_norm)
print("X norm + Y norm gives us: ", x_norm + y_norm)
print("\nThus, we show Triangle Inequality fulfilled!")

random_choice = [num for num in range(random.randint(3, 9))]
matrix = [[1,2, 3], [2,5,9], [1, 2, 4]]

print("\nMatrix A:")
for row in matrix:
    print(row)

print("\nPeforming square matrix transposal...")
matrix = matrix_transpose(matrix)
for row in matrix:
    print(row)
print("\n")
