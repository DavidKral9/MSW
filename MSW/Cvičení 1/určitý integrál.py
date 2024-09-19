import numpy as np
from scipy.integrate import quad
import time

# metoda Trapez python
def trapezoidal_rule(f, a, b, n=1000):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return result * h

def f(x):
    return np.sin(x)

start = time.time()
integral_python = trapezoidal_rule(f, 0, np.pi)
end = time.time()
print(f"Numerický integrál (Python): {end - start:.6f} s, Výsledek: {integral_python}")

# SciPy
start = time.time()
result, error = quad(f, 0, np.pi)
end = time.time()
print(f"Numerický integrál (SciPy): {end - start:.6f} s, Výsledek: {result}")

