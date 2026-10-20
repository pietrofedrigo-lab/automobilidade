import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('PIETRO GIOVANNE FEDRIGO - Automobile_data.csv')

# Ordenar por preço em ordem crescente (do mais barato ao mais caro)
df_ordenado = df.sort_values(by='price', ascending=True)

# Exibir a tabela ordenada
print(df_ordenado.to_string(index=False))