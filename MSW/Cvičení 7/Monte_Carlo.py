import numpy as np
import matplotlib.pyplot as plt
def monte_carlo_pi(num_points):
    # Počet bodů uvnitř kruhu
    inside_circle = 0
    
    # Generování náhodných bodů
    for _ in range(num_points):
        # Náhodné souřadnice x a y v rozmezí [-1, 1]
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        
        # Kontrola, zda bod spadá do kruhu (vzdálenost od středu <= 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    
    # Odhad π jako poměr bodů v kruhu k celkovému počtu bodů, vynásobený 4
    return (inside_circle / num_points) * 4
# Počet bodů pro simulaci
num_points = 1000000

# Odhad hodnoty π
pi_estimate = monte_carlo_pi(num_points)
print(f"Odhad hodnoty π pro {num_points} bodů: {pi_estimate}")

def monte_carlo_pi_visualize(num_points):
    inside_x = []
    inside_y = []
    outside_x = []
    outside_y = []
    
    # Generování náhodných bodů a jejich klasifikace
    for _ in range(num_points):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        
        if x**2 + y**2 <= 1:
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)
    
    # Vykreslení bodů
    plt.figure(figsize=(6,6))
    plt.scatter(inside_x, inside_y, color='blue', s=1, label='Uvnitř kruhu')
    plt.scatter(outside_x, outside_y, color='red', s=1, label='Mimo kruh')
    plt.title(f'Odhad π pomocí Monte Carlo s {num_points} body')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Vizualizace simulace
monte_carlo_pi_visualize(10000)
