import numpy as np
import time

A = np.array([[3, 2], [1, 4]])
B = np.array([7, 10])

# Řešení soustavy lineárních rovnic v Pythonu pomocí inverze matice
def inverse_matrix(A):
    n = len(A)
    A = A.astype(float)
    I = np.eye(n)
    for i in range(n):
        factor = A[i, i]
        for j in range(n):
            A[i, j] /= factor
            I[i, j] /= factor
        for k in range(n):
            if k != i:
                factor = A[k, i]
                for j in range(n):
                    A[k, j] -= factor * A[i, j]
                    I[k, j] -= factor * I[i, j]
    return I

start = time.time()
A_inv = inverse_matrix(A)
solution_python = A_inv.dot(B)
end = time.time()
print(f"Řešení soustavy (Python): {end - start:.6f} s, Řešení: {solution_python}")

# Řešení soustavy lineárních rovnic pomocí NumPy
start = time.time()
solution_numpy = np.linalg.solve(A, B)
end = time.time()
print(f"Řešení soustavy (NumPy): {end - start:.6f} s, Řešení: {solution_numpy}")

