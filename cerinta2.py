import pandas as pd
import matplotlib.pyplot as plt

# Citirea fișierului train.csv
file_path = 'train.csv'
data = pd.read_csv(file_path)

# Procentul persoanelor care au supraviețuit și care nu au supraviețuit
survival = 100 * data['Survived'].value_counts(normalize=True)

# Procentul bărbaților și femeilor
gender_counts = 100 * data['Sex'].value_counts(normalize=True)

# Procentul pasagerilor pentru fiecare tip de clasă
class_c = 100 * data['Pclass'].value_counts(normalize=True)

print(f"Procentul persoanelor care au supraviețuit: {survival[1]:.2f}%")
print(f"Procentul persoanelor care nu au supraviețuit: {survival[0]:.2f}%")
print("\nProcentul pasagerilor pentru fiecare tip de clasă:")
print(class_c)
print("\nProcentul bărbaților și femeilor:")
print(gender_counts)

