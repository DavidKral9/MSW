import numpy as np
import matplotlib.pyplot as plt
# Definování funkce a její derivace
def func(x):
    return np.sin(x)

def analytic_deriv(x):
    return np.cos(x)

# Dopředná diference (statický krok)
def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

# Centrální diference (statický krok)
def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)
def adaptive_difference(f, x, tol=1e-6):
    h = 1e-1 
    prev_deriv = (f(x + h) - f(x - h)) / (2 * h)
    
    while True:
        h /= 2
        deriv = (f(x + h) - f(x - h)) / (2 * h)
        
        # Pokud je rozdíl mezi derivacemi menší než tolerance, zastavíme adaptaci kroku
        if np.abs(deriv - prev_deriv) < tol:
            break
        prev_deriv = deriv
    
    return deriv, h

# Vstupní data
x_values = np.linspace(0, 2*np.pi, 100)
h_static = 0.01  # Statický krok

# Analytická derivace
y_analytic = analytic_deriv(x_values)

# Derivace pomocí dopředné a centrální diference (statický krok)
y_forward_static = forward_difference(func, x_values, h_static)
y_central_static = central_difference(func, x_values, h_static)

# Derivace s adaptabilním krokem
y_adaptive = []
h_values = []
for x in x_values:
    deriv, h_used = adaptive_difference(func, x)
    y_adaptive.append(deriv)
    h_values.append(h_used)

y_adaptive = np.array(y_adaptive)

# Vykreslení výsledků
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_analytic, label='Analytická derivace', color='blue')
plt.plot(x_values, y_forward_static, label='Dopředná diference (statický krok)', linestyle='--', color='green')
plt.plot(x_values, y_central_static, label='Centrální diference (statický krok)', linestyle='--', color='orange')
plt.plot(x_values, y_adaptive, label='Adaptabilní krok', linestyle='--', color='red')
plt.title('Porovnání numerické derivace se statickým a adaptabilním krokem')
plt.xlabel('x')
plt.ylabel('f\'(x)')
plt.legend()
plt.grid(True)
plt.show()

# Zobrazení adaptovaných kroků
plt.figure(figsize=(10, 6))
plt.plot(x_values, h_values, label='Adaptabilní krok h', color='purple')
plt.title('Velikost kroku h v závislosti na x (adaptabilní metoda)')
plt.xlabel('x')
plt.ylabel('h')
plt.grid(True)
plt.show()
