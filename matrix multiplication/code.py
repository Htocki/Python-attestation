# Перемножить две квадратные матрицы.
# Размерность матрицы задается с клавиатуры.

import numpy
import random

print("Enter dimension: ")
count = int(input())
lower_bound = 0
upper_bound = 9

A = numpy.matrix(
    [[random.randint(lower_bound, upper_bound) for i in range(count)]
    for j in range(count)])
print("\nMatrix A:\n", A)

B = numpy.matrix(
    [[random.randint(lower_bound, upper_bound) for i in range(count)]
    for j in range(count)])
print("\nMatrix B:\n", B)

C = A.dot(B)
print("\nMatrix C:\n", C)
