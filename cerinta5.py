import pandas as pd
import matplotlib.pyplot as plt

file_path = 'train.csv'
data = pd.read_csv(file_path)

# Definesc categoriile de vârstă
category = [0, 20, 40, 60, data['Age'].max()]
age_labels = ['0-20', '21-40', '41-60', '61+']

# Creez o coloana suplimentara pentru categoria de vârstă
data['AgeCategory'] = pd.cut(data['Age'], bins=category, labels=age_labels, right=True)

# Vizualizez primele rânduri pentru a verifica coloana nouă
print(data[['Age', 'AgeCategory']].head(10))

# Determin nr de pasageri pentru fiecare categorie de vârstă
counts = data['AgeCategory'].value_counts().sort_index()

print("\nNr de pasageri pentru fiecare categorie de vârstă:")
print(counts)

# Creez unui grafic pentru a evidenția rezultatele
plt.figure(figsize=(10, 6))
counts.plot(kind='bar', color='skyblue')
plt.title('Numărul de pasageri pentru fiecare categorie de vârstă')
plt.xlabel('Categorie de vârstă')
plt.ylabel('Număr de pasageri')
plt.xticks(rotation=0)
plt.show()
