import pandas as pd

nome_arquivo = 'PIETRO GIOVANNE FEDRIGO - Automobile_data.csv'

# 1. Carregar o arquivo reconhecendo valores nulos ('?', 'n.a', vazios)
df = pd.read_csv(nome_arquivo, na_values=['?', 'n.a', 'NaN', ''])

# 2. Remover linhas que possuem valores nulos na coluna 'price' (ou em qualquer coluna)
df_limpo = df.dropna(subset=['price'])

# 3. Remover linhas duplicadas
df_limpo = df_limpo.drop_duplicates()

# 4. Sobrescrever e atualizar o arquivo CSV original
df_limpo.to_csv(nome_arquivo, index=False)

print("Conjunto de dados limpo e arquivo CSV atualizado com sucesso!")