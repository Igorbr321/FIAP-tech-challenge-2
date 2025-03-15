import pandas as pd


'---------------------------------------------------------------------------------------------------------------'

def table_info(df):
    """
    Exibe informações resumidas da tabela:
    - Dimensões
    - Tipos de dados
    - Quantidade de valores nulos
    - Quantidade de valores únicos
    - Exemplo de valores por coluna
    """
    
    print("🔹 Dimensões do DataFrame:", df.shape)
    print("\n🔹 Tipos de dados:")
    print(df.dtypes)
    
    print("\n🔹 Valores nulos por coluna:")
    print(df.isnull().sum())

    print("\n🔹 Valores únicos por coluna:")
    print(df.nunique())

    print("\n🔹 Exemplos de valores por coluna:")
    print(df.head(3).T)  # Transposto para facilitar visualização por coluna

'---------------------------------------------------------------------------------------------------------------'







