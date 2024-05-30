import pandas as pd
import matplotlib.pyplot as plt

file_path = 'train.csv'
data = pd.read_csv(file_path)

# Setez o coloana suplimentare pentru a indica dacă persoana este copil sau adult
data['IsChild'] = data['Age'] < 18

# Calculez procentului copiilor aflați la bord
no_child = data['IsChild'].sum()
total = data.shape[0]
percentage_children = 100 * (no_child / total)

print(f"Procentul copiilor de la bord: {percentage_children:.2f}%")

# Calculez rata de supraviețuire pentru copii și adulți
rates = 100 * data.groupby('IsChild')['Survived'].mean()

print("\nRata de supraviețuire pentru copii și adulți este:")
print(rates)

# Crearea unui grafic pentru a evidenția rata de supraviețuire pentru copii și adulți
labels = ['Adulți', 'Copii']
rates.index = labels

plt.figure(figsize=(10, 6))
rates.plot(kind='bar', color=['skyblue', 'orange'])
plt.title('Rata de supraviețuire pentru copii și adulți')
plt.xlabel('Categorie')
plt.ylabel('Procent de supraviețuire (%)')
plt.xticks(rotation=0)
plt.show()
