import pandas as pd

# 1. Criar os dois dicionários
Car_Price = {
    'Company': ['Toyota', 'Honda', 'BMW', 'Audi'],
    'Price': [23845, 17995, 135925, 71400]
}

car_HorsePower = {
    'Company': ['Toyota', 'Honda', 'BMW', 'Audi'],
    'horsepower': [141, 80, 182, 160]
}

# 2. Criar os dois DataFrames
df_preco = pd.DataFrame(Car_Price)
df_potencia = pd.DataFrame(car_HorsePower)

# 3. Mesclar (merge) adicionando a coluna 'horsepower' ao primeiro DataFrame
df_resultado = pd.merge(df_preco, df_potencia, on='Company')

# Exibir o resultado
print(df_resultado)