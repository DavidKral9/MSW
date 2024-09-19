import time
import random
import hashlib
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
mouse_data = []

def on_move(x, y):
    mouse_data.append((x, y)) 

# Funkce pro sledování pohybu myši po dobu 5 sekund
def collect_mouse_data():
    with MouseListener(on_move=on_move) as listener:
        time.sleep(5) 
        listener.stop()

print("Pohybujte myší po dobu 5 sekund...")
collect_mouse_data()
print(f"Nasbíraná data o pohybu myši: {mouse_data}")
keyboard_data = []

def on_press(key):
    try:
        keyboard_data.append(str(key))  
    except AttributeError:
        pass  

# Funkce pro sledování úhozů po dobu 5 sekund
def collect_keyboard_data():
    with KeyboardListener(on_press=on_press) as listener:
        time.sleep(5)
        listener.stop()

print("Zadejte náhodné úhozy na klávesnici po dobu 5 sekund...")
collect_keyboard_data()
print(f"Nasbíraná data z klávesnice: {keyboard_data}")
current_time = time.time() 
print(f"Aktuální čas: {current_time}")



combined_data = f"{mouse_data}{keyboard_data}{current_time}"

# Hashování dat pomocí SHA-256 pro vytvoření semínka
seed = hashlib.sha256(combined_data.encode('utf-8')).hexdigest()

print(f"Vytvořené semínko: {seed}")
# Konverze semínka na číslo a inicializace generátoru
numeric_seed = int(seed, 16)
random.seed(numeric_seed)

random_number = random.randint(1, 100)
print(f"Náhodné číslo generované na základě vlastního semínka: {random_number}")
