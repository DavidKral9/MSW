import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = sns.load_dataset('titanic')
df.dropna(inplace=True)

# Přežití podle věku a pohlaví
plt.figure(figsize=(12, 6))
sns.violinplot(data=df, x='sex', y='age', hue='survived', split=True, inner='quart', palette={0: "r", 1: "g"})
plt.title('Přežití na Titanicu podle věku a pohlaví', fontsize=16)
plt.xlabel('Pohlaví', fontsize=14)
plt.ylabel('Věk', fontsize=14)
plt.legend(title='Přežití', loc='upper right', labels=['Nepřežili', 'Přežili'])
plt.grid(True)
plt.show()