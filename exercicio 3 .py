import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('PIETRO GIOVANNE FEDRIGO - Automobile_data.csv')

# 1. Montadora com o carro mais caro
carro_mais_caro = df[df['price'] == df['price'].max()]
print("--- Montadora do carro mais caro ---")
print(carro_mais_caro[['company', 'price']].to_string(index=False))

# 2. Montadora com a maior média de preço
media_por_empresa = df.groupby('company')['price'].mean().reset_index()
mais_cara_media = media_por_empresa.sort_values(by='price', ascending=False).iloc[0]

print("\n--- Montadora com maior preço médio ---")
print(f"Empresa: {mais_cara_media['company']} | Média: {mais_cara_media['price']:.2f}")