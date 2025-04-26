import pandas as pd
from pyswip import Prolog
from mlxtend.frequent_patterns import apriori, association_rules

# Inicializar Prolog
prolog = Prolog()
prolog.consult('movies.pl')

# Función para obtener películas y géneros
def obtener_peliculas():
    peliculas_data = []
    for pelicula in prolog.query("pelicula(Name, Genres)"):
        peliculas_data.append((pelicula['Name'], [str(genre) for genre in pelicula['Genres']]))
    return peliculas_data

# Obtener datos de películas
data = obtener_peliculas()
df = pd.DataFrame(data, columns=['pelicula', 'generos'])

# Crear un DataFrame para Apriori
def crear_dataframe_apriori(df):
    from sklearn.preprocessing import MultiLabelBinarizer

    mlb = MultiLabelBinarizer()
    generos_encoded = mlb.fit_transform(df['generos'])
    
    # Convertir a DataFrame con tipo booleano
    return pd.DataFrame(generos_encoded, columns=mlb.classes_).astype(bool)

# Función para recomendar películas basadas en estado de ánimo
def recomendar_peliculas_por_animo(estado_animo):
    estado_animo_generos = {
        "feliz": ["comedia", "animacion"],
        "triste": ["drama"],
        "emocionado": ["accion"],
        "pensativo": ["drama"],
    }

    generos_asociados = estado_animo_generos.get(estado_animo, [])
    if not generos_asociados:
        return "No hay recomendaciones disponibles."

    # Crear DataFrame para Apriori
    df_apriori = crear_dataframe_apriori(df)
    
    # Aplicar Apriori
    frequent_itemsets = apriori(df_apriori, min_support=0.05, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

    # Filtrar reglas que contienen los géneros asociados
    recomendaciones = rules[rules['antecedents'].apply(lambda x: any(genre in x for genre in generos_asociados))]
    
    # Obtener películas recomendadas
    peliculas_recomendadas = []
    for _, row in recomendaciones.iterrows():
        for genre in row['consequents']:
            peliculas_recomendadas.extend(df[df['generos'].apply(lambda x: genre in x)]['pelicula'].tolist())

    return list(set(peliculas_recomendadas))[:6]