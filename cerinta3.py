import pandas as pd
import matplotlib.pyplot as plt

file_path = 'train.csv'
data = pd.read_csv(file_path)

# Selectez coloanele numerice
columns = ['Age', 'SibSp', 'Parch', 'Fare']

# Configurez graficele
obj, axs = plt.subplots(len(columns), 1, figsize=(10, 20))

# Generez histograme pentru fiecare coloana
for i, column in enumerate(columns):
    axs[i].hist(data[column].dropna(), bins=30, color='c', edgecolor='k', alpha=0.7)
    axs[i].set_title(f'Histogramă pentru {column}')
    axs[i].set_xlabel(column)
    axs[i].set_ylabel('Frecvență')

# Ajustez layout-ului
plt.tight_layout()
plt.show()
