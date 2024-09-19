import numpy as np
import time

# numerická metoda python
def find_roots(coefficients, tolerance=1e-6, max_iterations=1000):
    roots = []
    poly = np.poly1d(coefficients)
    deriv = poly.deriv()
    
    for i in range(len(coefficients) - 1):
        root = np.random.rand()
        for _ in range(max_iterations):
            root_new = root - poly(root) / deriv(root)
            if abs(root_new - root) < tolerance:
                break
            root = root_new
        roots.append(root)
        coefficients = np.polydiv(coefficients, [1, -root])[0]
        poly = np.poly1d(coefficients)
        deriv = poly.deriv()
    
    return roots

coefficients = [1, -6, 11, -6]

start = time.time()
roots_python = find_roots(coefficients)
end = time.time()
print(f"Kořeny polynomu (Python): {end - start:.6f} s, Kořeny: {roots_python}")

# NumPy
start = time.time()
roots_numpy = np.roots(coefficients)
end = time.time()
print(f"Kořeny polynomu (NumPy): {end - start:.6f} s, Kořeny: {roots_numpy}")
