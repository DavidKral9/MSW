import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = sns.load_dataset('titanic')

# Korelace mezi numerickými atributy
plt.figure(figsize=(12, 10))
numerical_cols = ['age', 'fare', 'sibsp', 'parch']
corr_matrix = df[numerical_cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Korelační matice numerických atributů cestujících', fontsize=16)
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()