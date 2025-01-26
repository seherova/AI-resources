import numpy as np


A = np.array([[-1,1], [0,1], [2,1]])
B = np.array([[1], [1], [1]])

#A_T
A_T = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
for i in range(len(A)):
    for j in range(len(A[0])):
        A_T[j][i] = A[i][j]
#A_T_A
A_T_A = [[0 for _ in range(len(A_T[0]))] for _ in range(len(A_T))]
#len(A)
for i in range(len(A_T)):
    for j in range(len(A[0])):
        for k in range(len(A)):
            A_T_A[i][j] += A_T[i][k] * A[k][j]
            
#A_T_B
A_T_B = [[0 for _ in range(len(B[0]))] for _ in range(len(A_T))]
for i in range(len(A_T)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            A_T_B[i][j] += A_T[i][k] * B[k][j]

#det(A_T_A)
det_A_T_A = ((A_T_A[0][0]* A_T_A[1][1]) - A_T_A[0][1]* A_T_A[1][0])

# adjoint of A_T_A
adj_A_T_A = [
        [A_T_A[1][1], -A_T_A[0][1]],
        [-A_T_A[1][0], A_T_A[0][0]]
        ]

# inverse of A_T_A
inv_A_T_A = [[0 for _ in range(len(adj_A_T_A[0]))] for _ in range(len(adj_A_T_A))]
for i in range(len(adj_A_T_A)):
    for j in range(len(adj_A_T_A[0])):
        inv_A_T_A[i][j] = adj_A_T_A[i][j] / det_A_T_A

# X = (A^T * A)^(-1) * (A^T * B)

X = [[0 for _ in range(len(A_T_B[0]))] for _ in range(len(inv_A_T_A))]
for i in range(len(inv_A_T_A)):
    for j in range(len(A_T_B[0])):
        for k in range(len(A_T_B)):
            X[i][j] += inv_A_T_A[i][k] * A_T_B[k][j]

print("A^T * A:")
for row in A_T_A:
    print(row)

print("\nDeterminant of A^T * A:", det_A_T_A)

print("\nAdjoint of A^T * A:")
for row in adj_A_T_A:
    print(row)

print("\nInverse of A^T * A:")
for row in inv_A_T_A:
    print(row)

print("\nA^T * B:")
for row in A_T_B:
    print(row)

print("\nSolution X:")
for row in X:
    print(row)



## a_t_b 1 - 3
