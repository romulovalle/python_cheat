#Using Jupyter: !pip install pandas

#Import Pandas lib
import pandas as pd

# Criando um DataFrame
data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Idade': [25, 30, 35, 40, None],
    'Gênero': ['F', 'M', 'M', 'M', 'F'],
    'Salário': [50000, 60000, 75000, None, 45000]
}

df = pd.DataFrame(data)

# 1. Visualizando os primeiros registros do DataFrame
df.head()

# 2. Verificando a estrutura do DataFrame
df.info()

# 3. Lidando com dados ausentes (preenchendo com valores de média e mediana padrão)
df.fillna({'Idade': df['Idade'].mean(), 'Salário': df['Salário'].median()}, inplace=True)
print(df)

# 4. Filtrando dados com base em condições específicas
filter = df[df['Idade'] > 30]
filter = df[df['Idade'] = 30]
filter = df[df['Nome'] = 'Alice']

# 5. Calculando estatísticas resumidas
df.describe()

# 6. Operações de estatísticas descritivas
df['Idade'].mean()
df['Salário'].min()
df['Salário'].max()
df['Salário'].mode()
df['Salário'].std()
df['Salário'].var()
df['Salário'].quantile(q)
df['Salário'].cumsum()
df['Salário'].cumprod()
df['Salário'].value_counts()
df['Salário'].skew()
df['Salário'].kurtosis()

# 10. Importar e Exportar dados
df.to_csv('dados.csv', index=False)
df.read_csv('raw_dados.csv', index=False)
df.to_excel('dados.csv', index=False)
df.read_excel('raw_dados.csv', index=False)
