import numpy as np
import time
from scipy.optimize import bisect, newton
# Polynomiální funkce
def poly_function(x):
    return x**3 - 6*x**2 + 4*x + 12

# Exponenciální funkce
def exp_function(x):
    return np.exp(x) - 5

# Harmonická funkce
def harmonic_function(x):
    return np.sin(x) - 0.5
# Uzavřená metoda - Bisection Method
def find_root_bisection(f, a, b):
    start_time = time.time()
    root = bisect(f, a, b)
    duration = time.time() - start_time
    return root, duration
# Derivace funkcí pro Newtonovu metodu
def poly_function_deriv(x):
    return 3*x**2 - 12*x + 4

def exp_function_deriv(x):
    return np.exp(x)

def harmonic_function_deriv(x):
    return np.cos(x)

# Otevřená metoda - Newtonova metoda
def find_root_newton(f, f_prime, x0):
    start_time = time.time()
    root = newton(f, x0, fprime=f_prime)
    duration = time.time() - start_time
    return root, duration
# Polynomiální funkce
root_bisect_poly, time_bisect_poly = find_root_bisection(poly_function, -10, 10)
root_newton_poly, time_newton_poly = find_root_newton(poly_function, poly_function_deriv, 0)

print("Polynomiální funkce:")
print(f"  Bisection method: kořen = {root_bisect_poly}, čas = {time_bisect_poly:.6f} s")
print(f"  Newton method: kořen = {root_newton_poly}, čas = {time_newton_poly:.6f} s")

# Exponenciální funkce
root_bisect_exp, time_bisect_exp = find_root_bisection(exp_function, 0, 3)
root_newton_exp, time_newton_exp = find_root_newton(exp_function, exp_function_deriv, 1)

print("\nExponenciální funkce:")
print(f"  Bisection method: kořen = {root_bisect_exp}, čas = {time_bisect_exp:.6f} s")
print(f"  Newton method: kořen = {root_newton_exp}, čas = {time_newton_exp:.6f} s")

# Harmonická funkce
root_bisect_harmonic, time_bisect_harmonic = find_root_bisection(harmonic_function, 0, 2)
root_newton_harmonic, time_newton_harmonic = find_root_newton(harmonic_function, harmonic_function_deriv, 1)

print("\nHarmonická funkce:")
print(f"  Bisection method: kořen = {root_bisect_harmonic}, čas = {time_bisect_harmonic:.6f} s")
print(f"  Newton method: kořen = {root_newton_harmonic}, čas = {time_newton_harmonic:.6f} s")
# Vyhodnocení přesnosti
def compare_accuracy(root_bisect, root_newton):
    return abs(root_bisect - root_newton)

print("\nPorovnání přesnosti:")
print(f"  Polynomiální funkce: |kořen bisekce - kořen Newton| = {compare_accuracy(root_bisect_poly, root_newton_poly):.6f}")
print(f"  Exponenciální funkce: |kořen bisekce - kořen Newton| = {compare_accuracy(root_bisect_exp, root_newton_exp):.6f}")
print(f"  Harmonická funkce: |kořen bisekce - kořen Newton| = {compare_accuracy(root_bisect_harmonic, root_newton_harmonic):.6f}")
