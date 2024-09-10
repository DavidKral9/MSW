import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.sparse.linalg import bicgstab

# Přímá metoda (NumPy `linalg.solve`)
def direct_method(A, b):
    return np.linalg.solve(A, b)

# Iterační metoda (Jacobiho metoda implementovaná pomocí `bicgstab`)
def iterative_method(A, b):
    x, exitCode = bicgstab(A, b, atol=1e-10, maxiter=1000)
    return x

# Generování náhodných čtvercových matic a vektorů
def generate_matrix_and_vector(size):
    A = np.random.rand(size, size)
    b = np.random.rand(size)
    return A, b

# Měření času a vytváření grafů
matrix_sizes = [10, 50, 100, 200, 500, 1000, 1250, 1500, 1750, 2000]  # Různé velikosti matic
direct_times = []
iterative_times = []

for size in matrix_sizes:
    A, b = generate_matrix_and_vector(size)
    
    # Přímá metoda
    start_time = time.time()
    direct_method(A, b)
    direct_time = time.time() - start_time
    direct_times.append(direct_time)
    
    # Iterační metoda
    start_time = time.time()
    iterative_method(A, b)
    iterative_time = time.time() - start_time
    iterative_times.append(iterative_time)

# Vytvoření grafu
plt.figure(figsize=(10, 6))
plt.plot(matrix_sizes, direct_times, label='Přímá metoda (NumPy)', marker='o')
plt.plot(matrix_sizes, iterative_times, label='Iterační metoda (bicgstab)', marker='o')
plt.xlabel('Velikost matice')
plt.ylabel('Průměrný čas (s)')
plt.title('Porovnání přímé a iterační metody pro různé velikosti matic')
plt.legend()
plt.grid(True)
plt.show()