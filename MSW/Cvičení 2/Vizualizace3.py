import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = sns.load_dataset('titanic')
df.dropna(inplace=True)


# Vztah mezi věkem a jízdným
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='age', y='fare', hue='class', style='who', s=100, alpha=0.7)
plt.title('Vztah mezi věkem a jízdným na Titanicu podle třídy a statusu', fontsize=16)
plt.xlabel('Věk', fontsize=14)
plt.ylabel('Jízdné ($)', fontsize=14)
plt.legend(title='Třída & Status', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()