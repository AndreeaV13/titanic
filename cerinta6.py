import pandas as pd
import matplotlib.pyplot as plt

file_path = 'train.csv'
data = pd.read_csv(file_path)

# Definesc categoriile de vârstă
category = [0, 20, 40, 60, data['Age'].max()]
age_labels = ['0-20', '21-40', '41-60', '61+']

# Crearea unei coloane suplimentare pentru categoria de vârstă
data['AgeCategory'] = pd.cut(data['Age'], bins=category, labels=age_labels, right=True)

# Vizualizez primele rânduri pentru a verifica coloana nouă
print(data[['Age', 'AgeCategory']].head(10))

# Filtrez datele pentru bărbați
male_data = data[data['Sex'] == 'male']

# Determin nr de bărbați care au supraviețuit pentru fiecare categorie de vârstă
survival_males = male_data.groupby('AgeCategory', observed=False)['Survived'].sum()

print("\nNr de bărbați care au supraviețuit:")
print(survival_males)

# Calculez nr total de bărbați în fiecare categorie de vârstă
total_males = male_data['AgeCategory'].value_counts().sort_index()

# Calculez procentul de supraviețuire pentru bărbați în fiecare categorie de vârstă
survival_perc = 100 * (survival_males / total_males)

print("\nProcentul de supraviețuire al bărbaților pentru fiecare categorie de vârstă:")
print(survival_perc)

# Creez graficul
plt.figure(figsize=(10, 6))
survival_perc.plot(kind='bar', color='skyblue')
plt.title('Procentul de supraviețuire al bărbaților pe categorii de vârstă')
plt.xlabel('Categoria de vârstă')
plt.ylabel('Procentul de supraviețuire (%)')
plt.xticks(rotation=0)
plt.show()
