import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'train_filled.csv'
data = pd.read_csv(file_path)

# Extrag titlurile din coloana `Name`
data['Title'] = data['Name'].str.extract(r',\s*([^\.]*)\s*\.', expand=False)

# Verific coresp titlurilor cu sexul persoanei
title_gender_map = {
    'Mr': 'male',
    'Mrs': 'female',
    'Miss': 'female',
    'Master': 'male',
    'Don': 'male',
    'Rev': 'male',
    'Dr': 'both', 
    'Mme': 'female',
    'Ms': 'female',
    'Major': 'male',
    'Lady': 'female',
    'Sir': 'male',
    'Mlle': 'female',
    'Col': 'male',
    'Capt': 'male',
    'Countess': 'female',
    'Jonkheer': 'male',
    'Dona': 'female'
}

data['Title_Gender'] = data['Title'].map(title_gender_map)

# Verific corespondența
data['Title_Matches_Sex'] = data.apply(lambda row: row['Sex'] == row['Title_Gender'] or row['Title_Gender'] == 'both', axis=1)

# Nr de persoane pentru fiecare titlu
title_count = data['Title'].value_counts()

# Reprezint grafic distribuția titlurilor
plt.figure(figsize=(10, 6))
sns.countplot(y='Title', data=data, order=title_count.index, palette='viridis')
plt.title('Distribuția titlurilor')
plt.xlabel('Nr de persoane')
plt.ylabel('Titlul')
plt.show()

# Verific corectitudinii titlurilor
incorrect_titles = data[~data['Title_Matches_Sex']]
correct_titles_count = data['Title_Matches_Sex'].sum()
incorrect_titles_count = len(data) - correct_titles_count

print(f"Numărul de titluri corecte sunt: {correct_titles_count}")
print(f"Numărul de titluri incorecte sunt: {incorrect_titles_count}")
print(f"\nTitluri incorecte sunt:\n{incorrect_titles[['Name', 'Title', 'Sex']]}")

# Verificare suplimentară a titlurilor și a spațiilor
unique_titles = data['Title'].unique()
print(f"\nTitluri unice în date:\n{unique_titles}")
