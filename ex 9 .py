import pandas as pd

# 1. Definir os dois dicionários
GermanCars = {
    'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'],
    'Price': [23845, 171995, 135925, 71400]
}

japaneseCars = {
    'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '],
    'Price': [29995, 23600, 61500, 58900]
}

# 2. Criar os dois DataFrames
df_german = pd.DataFrame(GermanCars)
df_japanese = pd.DataFrame(japaneseCars)

# 3. Concatenar os DataFrames usando chaves para identificar a origem (Alemanha e Japão)
df_concat_keys = pd.concat([df_german, df_japanese], keys=['Germany', 'Japan'])

print("--- Resultado com identificação de origem (keys) ---")
print(df_concat_keys)


# Opção alternativa: Concatenar em uma lista única contínua (ignore_index=True)
df_concat_unico = pd.concat([df_german, df_japanese], ignore_index=True)

print("\n--- Resultado com índice unificado (ignore_index=True) ---")
print(df_concat_unico)