import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'train_filled.csv'
data = pd.read_csv(file_path)

# Creez o coloana pentru a indica dacă un pasager este singur (nu are rude pe vas)
data['IsAlone'] = (data['SibSp'] + data['Parch'] == 0).astype(int)

# Analizaez influența stării de a fi singur asupra șanselor de supraviețuire
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='IsAlone', hue='Survived', multiple='stack', bins=3)
plt.title('Influența stării de a fi singur asupra șanselor de supraviețuire')
plt.xlabel('Starea de a fi singur (0 = Nu, 1 = Da)')
plt.ylabel('Numărul de persoane')
plt.xticks([0, 1], ['Nu', 'Da'])
plt.show()

# relația dintre tarif, clasă și starea de supraviețuire pentru primele 100 de înregistrări
subset = data.head(100)

plt.figure(figsize=(12, 8))
sns.catplot(data=subset, x='Pclass', y='Fare', hue='Survived', kind='swarm', height=6, aspect=1.5)
plt.title('Relația dintre tarif, clasă și starea de supraviețuire pentru primele 100 de înregistrări')
plt.xlabel('Clasa')
plt.ylabel('Tarif')
plt.show()
