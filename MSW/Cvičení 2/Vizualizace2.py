import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Načtení datasetu Titanic
df = sns.load_dataset('titanic')
df.dropna(inplace=True)


# Vizualizace 2: Průměrné jízdné podle třídy
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='class', y='fare', hue='class', palette='viridis', errorbar=None, legend=False)
plt.title('Průměrné jízdné podle třídy na Titanicu', fontsize=16)
plt.xlabel('Třída', fontsize=14)
plt.ylabel('Průměrné jízdné ($)', fontsize=14)
plt.grid(True)
plt.show()
