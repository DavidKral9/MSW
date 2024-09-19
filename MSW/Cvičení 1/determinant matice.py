import numpy as np
import time

A = np.array([[3, 2], [1, 4]])
# rekurzivní metoda python
def determinant_recursive(A):
    if len(A) == 2:
        return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]

    det = 0
    for c in range(len(A)):
        submatrix = np.delete(np.delete(A, 0, axis=0), c, axis=1)
        det += ((-1) ** c) * A[0, c] * determinant_recursive(submatrix)
    return det
start = time.time()
det_python = determinant_recursive(A)
end = time.time()
print(f"Determinant (Python): {end - start:.6f} s, Determinant: {det_python}")

# NumPy
start = time.time()
det_numpy = np.linalg.det(A)
end = time.time()
print(f"Determinant (NumPy): {end - start:.6f} s, Determinant: {det_numpy}")