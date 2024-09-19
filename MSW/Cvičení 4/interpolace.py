import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, lagrange, CubicSpline
from numpy.polynomial.polynomial import Polynomial


def poly_function(x):
    return x**3 - 6*x**2 + 4*x + 12

def harmonic_function(x):
    return np.sin(x)

def log_function(x):
    return np.log(x)


x_values = np.linspace(1, 10, 10)



y_poly = poly_function(x_values)
y_harmonic = harmonic_function(x_values)
y_log = log_function(x_values)

# Lineární interpolace
linear_interp_poly = interp1d(x_values, y_poly, kind='linear')
linear_interp_harmonic = interp1d(x_values, y_harmonic, kind='linear')
linear_interp_log = interp1d(x_values, y_log, kind='linear')

# Lagrangeova interpolace
lagrange_interp_poly = lagrange(x_values, y_poly)
lagrange_interp_harmonic = lagrange(x_values, y_harmonic)
lagrange_interp_log = lagrange(x_values, y_log)

# Spline interpolace
spline_interp_poly = CubicSpline(x_values, y_poly)
spline_interp_harmonic = CubicSpline(x_values, y_harmonic)
spline_interp_log = CubicSpline(x_values, y_log)
x_new = np.linspace(1, 10, 100)  # Vytvoříme nové jemné hodnoty pro interpolaci

# graf pro polynomiální funkci
plt.figure(figsize=(10, 6))
plt.plot(x_new, poly_function(x_new), label='Skutečná funkce', color='blue')
plt.plot(x_new, linear_interp_poly(x_new), label='Lineární interpolace', linestyle='--', color='green')
plt.plot(x_new, lagrange_interp_poly(x_new), label='Lagrangeova interpolace', linestyle='--', color='orange')
plt.plot(x_new, spline_interp_poly(x_new), label='Spline interpolace', linestyle='--', color='red')
plt.scatter(x_values, y_poly, color='black', label='Vzorkované body')
plt.title('Polynomiální funkce - Interpolace')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# graf pro harmonickou funkci
plt.figure(figsize=(10, 6))
plt.plot(x_new, harmonic_function(x_new), label='Skutečná funkce', color='blue')
plt.plot(x_new, linear_interp_harmonic(x_new), label='Lineární interpolace', linestyle='--', color='green')
plt.plot(x_new, lagrange_interp_harmonic(x_new), label='Lagrangeova interpolace', linestyle='--', color='orange')
plt.plot(x_new, spline_interp_harmonic(x_new), label='Spline interpolace', linestyle='--', color='red')
plt.scatter(x_values, y_harmonic, color='black', label='Vzorkované body')
plt.title('Harmonická funkce - Interpolace')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# graf pro logaritmickou funkci
plt.figure(figsize=(10, 6))
plt.plot(x_new, log_function(x_new), label='Skutečná funkce', color='blue')
plt.plot(x_new, linear_interp_log(x_new), label='Lineární interpolace', linestyle='--', color='green')
plt.plot(x_new, lagrange_interp_log(x_new), label='Lagrangeova interpolace', linestyle='--', color='orange')
plt.plot(x_new, spline_interp_log(x_new), label='Spline interpolace', linestyle='--', color='red')
plt.scatter(x_values, y_log, color='black', label='Vzorkované body')
plt.title('Logaritmická funkce - Interpolace')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
