#VOINEA ANDREEA-GABRIELA, GRUPA 313CB, PARTEA 1

import pandas as pd

# Citesc fișierului train.csv
file_path = 'train.csv'
data = pd.read_csv(file_path)

typee = data.dtypes
no_col = data.shape[1]
no_rows = data.shape[0]
missing_values = data.isnull().sum()
dupp_rows = data.duplicated().sum()

# Afisez rezultatele
print(f"Nr coloane: {no_col}")
print("\n")
print("Tipuri de date pentru coloane:")
print(typee)
print("\nNr valori lipsă pentru coloane:")
print(missing_values)
print(f"\nNr linii: {no_rows}")
print(f"Nr linii duplicate: {dupp_rows}")
