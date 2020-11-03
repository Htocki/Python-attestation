# Решить систему линейных уравнений методом Гаусса.

def linearsolver(A, B):
  n = len(A)
  M = A

  i = 0
  for x in M:
   x.append(B[i])
   i += 1

  for k in range(n):
   for i in range(k, n):
     if abs(M[i][k]) > abs(M[k][k]):
        M[k], M[i] = M[i], M[k]
     else:
        pass

   for j in range(k+1, n):
       q = float(M[j][k]) / M[k][k]
       for m in range(k, n+1):
          M[j][m] -=  q * M[k][m]

  x = [0 for i in range(n)]

  x[n-1] =float(M[n-1][n])/M[n-1][n-1]
  for i in range (n-1,-1,-1):
    z = 0
    for j in range(i+1,n):
        z = z  + float(M[i][j])*x[j]
    x[i] = float(M[i][n] - z)/M[i][i]
  return x


A = [[1, 2, 3], [2, 1, 2], [3, 2, 1]]
print("Coefficient matrix:")
print(' [', A[0][0], A[0][1], A[0][2], ']')
print(' [', A[1][0], A[1][1], A[1][2], ']')
print(' [', A[2][0], A[2][1], A[2][2], ']')

B = [4, 3, 9]
print("\nColumn of free members:")
print(' [', B[0], ']')
print(' [', B[1], ']')
print(' [', B[2], ']')

X = linearsolver(A, B)
print("\nUnknowns column:")
print(' [', "%.3f" % (X[0]), ']')
print(' [', "%.3f" % (X[1]), ']')
print(' [', "%.3f" % (X[2]), ']')
