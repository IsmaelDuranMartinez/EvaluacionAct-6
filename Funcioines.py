def cuenta_valores_nulos(df):
    
    valores_nulos_cols = df.isnull().sum()
    valores_nulos_df = df.isnull().sum().sum()
    
    return("Valores nulos por columna", valores_nulos_cols,
            "Valores nulos por dataframe", valores_nulos_df)


def sustituir_nulos(df):
    import pandas as pd
    cuantitativas_con_nulos = df.select_dtypes(include=['float64', 'int64', 'float', 'int'])
    cualitativas = df.select_dtypes(include=['object', 'datetime', 'category'])
    
    cuantitativas = cuantitativas_con_nulos.copy()
    for i, col in enumerate(cuantitativas.columns):
        if i % 2 == 0:
            cuantitativas[col].fillna(round(cuantitativas[col].mean(), 1), inplace=True)
        else:
            cuantitativas[col].fillna(99, inplace=True)
    
    cualitativas.fillna("Este_es_un_valor_nulo", inplace=True)
    
    dfl= pd.concat([cuantitativas, cualitativas], axis=1)
    
    
def sustituir_atipicos(dfl):
            import pandas as pd
            for col in df.select_dtypes(include=['int64', 'float64']).columns:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                Iqr=Q1-Q3
                Limite_superior= Q3+ 1.5*Iqr
                Limite_inferior= Q1- 1.5*Iqr
                df[col] = np.where((df[col] < Limite_inferior) | (dfl[col] > Limite_superior), dfl[col].median(), dfl[col])
            
def cargar_archivo(archivo):
    import pandas as pd
    import os

    extension=os.path.splitext(archivo)[1].lower()
    """Carga archivos CSV o XLSX y los convierte en un DataFrame, sustituyendo valores nulos según la función 2."""
    if extension == '.csv':
        return(archivo)
                         
    elif extension == '.xlsx':
        return(archivo)
    else:
        raise ValueError(f"Este formato no está soportado para esta función: {extension}")
