import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('PIETRO GIOVANNE FEDRIGO - Automobile_data.csv')

# Agrupar por empresa e calcular a média da coluna 'average-mileage'
media_quilometragem = df.groupby('company')['average-mileage'].mean().reset_index()

# Arredondar os resultados para 2 casas decimais
media_quilometragem['average-mileage'] = media_quilometragem['average-mileage'].round(2)

# Exibir a tabela
print(media_quilometragem.to_string(index=False))