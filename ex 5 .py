import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('PIETRO GIOVANNE FEDRIGO - Automobile_data.csv')

# Agrupar por empresa, contando o total de carros e encontrando o maior preço
resultado = df.groupby('company').agg(
    total_carros=('company', 'count'),
    preco_mais_alto=('price', 'max')
).reset_index()

# Exibir o resultado
print(resultado.to_string(index=False))
