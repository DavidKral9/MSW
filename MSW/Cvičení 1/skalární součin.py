import numpy as np
import time

# Generování vektorů
a = np.random.rand(1000000)
b = np.random.rand(1000000)

# Skalární součin python
start = time.time()
dot_product_python = sum([a[i] * b[i] for i in range(len(a))])
end = time.time()
print(f"Skalární součin (Python): {end - start:.6f} s")

# Skalární součin NumPy
start = time.time()
dot_product_numpy = np.dot(a, b)
end = time.time()
print(f"Skalární součin (NumPy): {end - start:.6f} s")

