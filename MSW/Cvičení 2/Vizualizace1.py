import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Načtení datasetu Titanic
df = sns.load_dataset('titanic')
df.dropna(inplace=True)

# Vizualizace 1: Distribuce věku cestujících
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='age', bins=20, kde=True, color='skyblue')
plt.title('Distribuce věku cestujících na Titanicu', fontsize=16)
plt.xlabel('Věk', fontsize=14)
plt.ylabel('Počet cestujících', fontsize=14)
plt.grid(True)
plt.show()