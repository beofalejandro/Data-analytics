import pandas as pd
from pyswip import Prolog
from mlxtend.frequent_patterns import apriori, association_rules

prolog = Prolog()
prolog.consult('movies.pl')

# Función para obtener películas y géneros
def obtener_peliculas():
    peliculas_data = []
    for pelicula in prolog.query("pelicula(Name, Genres)"):
        if isinstance(pelicula['Genres'], str):
            genres = [pelicula['Genres']]
        else:
            genres = [str(genre) for genre in pelicula['Genres']]
        peliculas_data.append((pelicula['Name'], genres))
    return peliculas_data

data = obtener_peliculas()
df = pd.DataFrame(data, columns=['pelicula', 'generos'])

# Verificar películas en géneros específicos
def verificar_generos(generos):
    for genero in generos:
        peliculas_genero = df[df['generos'].apply(lambda x: genero in x)]
        print(f"Películas en el género '{genero}':")
        print(peliculas_genero['pelicula'].tolist())

# Llamar a la función de verificación
verificar_generos(["horror", "misterio"])

# Crear un DataFrame para Apriori
def crear_dataframe_apriori(df):
    from sklearn.preprocessing import MultiLabelBinarizer

    mlb = MultiLabelBinarizer()
    generos_encoded = mlb.fit_transform(df['generos'])
    return pd.DataFrame(generos_encoded, columns=mlb.classes_).astype(bool)

# Función para recomendar películas basadas en estado de ánimo
def recomendar_peliculas_por_animo(estado_animo):
    estado_animo_generos = {
        "feliz": ["comedia", "animacion"],
        "triste": ["drama"],
        "temeroso": ["horror", "misterio", "suspenso"],
        "emocionado": ["accion", "aventura"],
        "pensativo": ["drama", "documental"],
    }

    generos_asociados = estado_animo_generos.get(estado_animo, [])
    if not generos_asociados:
        return "No hay recomendaciones disponibles."

    df_apriori = crear_dataframe_apriori(df)
    frequent_itemsets = apriori(df_apriori, min_support=0.05, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)


    # Filtrar solo las reglas que llevan a los géneros asociados
    recomendaciones = []
    for genre in generos_asociados:
        filtered_rules = rules[rules['consequents'].apply(lambda x: genre in x)]
        for _, row in filtered_rules.iterrows():
            for antecedent in row['antecedents']:
                recomendaciones.extend(df[df['generos'].apply(lambda x: antecedent in x)]["pelicula"].tolist())

    recomendaciones = list(set(recomendaciones))
    if not recomendaciones:
        return f"No se encontraron recomendaciones para el estado de ánimo '{estado_animo}'."

    return recomendaciones[:6]