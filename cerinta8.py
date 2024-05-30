import pandas as pd

file_path = 'train.csv'
data = pd.read_csv(file_path)

# Calculez mediei vârstei pentru pasagerii care au supraviețuit și cei care nu au supraviețuit
age_surv = data[data['Survived'] == 1]['Age'].mean()
age_not_surv = data[data['Survived'] == 0]['Age'].mean()

# Funcție pentru completarea valorilor lipsă în coloana Age
def f(row):
    if pd.isnull(row['Age']):
        if row['Survived'] == 1:
            return age_surv
        else:
            return age_not_surv
    else:
        return row['Age']

# Aplicarea funcției pentru completarea valorilor lipsă în coloana `Age`
data['Age'] = data.apply(f, axis=1)

# Calcularea celei mai frecvente valori pentru `Embarked` în funcție de `Survived`
embarked_surv= data[data['Survived'] == 1]['Embarked'].mode()[0]
embarked_not_surv= data[data['Survived'] == 0]['Embarked'].mode()[0]

# Funcție pentru completarea valorilor lipsă în coloana `Embarked`
def function(row):
    if pd.isnull(row['Embarked']):
        if row['Survived'] == 1:
            return embarked_surv
        else:
            return embarked_not_surv
    else:
        return row['Embarked']

# Aplicarea funcției pentru completarea valorilor lipsă în coloana `Embarked`
data['Embarked'] = data.apply(function, axis=1)

# Calcularea celei mai frecvente valori pentru `Cabin` în funcție de `Survived`
mode_cabin_survived = data[data['Survived'] == 1]['Cabin'].mode()[0] if not data[data['Survived'] == 1]['Cabin'].mode().empty else 'Unknown'
mode_cabin_not_survived = data[data['Survived'] == 0]['Cabin'].mode()[0] if not data[data['Survived'] == 0]['Cabin'].mode().empty else 'Unknown'

# Funcție pentru completarea valorilor lipsă în coloana `Cabin`
def function2(row):
    if pd.isnull(row['Cabin']):
        if row['Survived'] == 1:
            return mode_cabin_survived
        else:
            return mode_cabin_not_survived
    else:
        return row['Cabin']

# Aplic funcției pentru completarea valorilor lipsă în coloana `Cabin`
data['Cabin'] = data.apply(function2, axis=1)

# Verific valorilor lipsă după completare
missing_values_after = data.isnull().sum()
print("\nValorile lipsă după completare sunt:")
print(missing_values_after)

# Salvez DataFrame-ului completat într-un nou fișier CSV
output_file_path = 'train_filled.csv'
data.to_csv(output_file_path, index=False)
print(f"\nFișierul completat a fost salvat la: {output_file_path}")
