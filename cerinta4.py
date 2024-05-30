import pandas as pd

file_path = 'train.csv'
data = pd.read_csv(file_path)

# Identific coloanelor cu val lipsă
m_data = data.isnull().sum()
m_col = m_data[m_data > 0]

print("Coloanele cu valori lipsă și nr lor:")
print(m_col)

# Calculez nr și proportia valorilor lipsă pentru fiecare coloană
total_rows = data.shape[0]
missing_info = pd.DataFrame({
    'Nr valorilor lipsă este': m_col,
    'Proporția valorilor lipsă este (%)': 100 * (m_col / total_rows)
})

print("\nNr și proporția valorilor lipsă pentru fiecare coloană:")
print(missing_info)

# Calculez procentul valorilor lipsă pentru fiecare clasă
def missing_perc(df, class_column, m_col):
    results = {}
    for column in m_col.index:
        procentt = df.groupby(class_column)[column].apply(lambda x: x.isnull().mean() * 100)
        results[column] = procentt
    return pd.DataFrame(results)

missing_per_class = missing_perc(data, 'Survived', m_col)

print("\nProcentul valorilor lipsă pentru fiecare clasă (Survived):")
print(missing_per_class)
