import pandas as pd
from pyswip import Prolog
from mlxtend.frequent_patterns import apriori, association_rules

prolog = Prolog()
prolog.consult('movies.pl')

# Function to obtain movies and their genres  
def obtener_peliculas():
    peliculas_data = []
    for pelicula in prolog.query("pelicula(Name, Genres)"):
        peliculas_data.append((pelicula['Name'], pelicula['Genres']))
    return peliculas_data

# Obtain movie data
data = obtener_peliculas()

if not data:
    print("No movies found.")
else:
    df = pd.DataFrame(data, columns=['pelicula', 'generos'])
    def create_transaction_list(df):
        return df['generos'].tolist()
    transaction_list = create_transaction_list(df)

    # Create a DataFrame for Apriori
    from mlxtend.preprocessing import TransactionEncoder
    encoder = TransactionEncoder()
    encoded_array = encoder.fit(transaction_list).transform(transaction_list)
    onehot_df = pd.DataFrame(encoded_array, columns=encoder.columns_)

    # Apply the Apriori algorithm to find frequent itemsets and association rules
    frequent_itemsets = apriori(onehot_df, min_support=0.05, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.05) 

    # Function to recommend movies based on the viewed movie
    def recomendar(pelicula_vista):
        if pelicula_vista not in df['pelicula'].values:
            return [] 
        
        generos = df.loc[df['pelicula'] == pelicula_vista, 'generos'].values[0]
        similar_movies = df[df['generos'].apply(lambda x: any(genre in x for genre in generos))]
        similar_movies = similar_movies[similar_movies['pelicula'] != pelicula_vista]
        similar_movies['shared_count'] = similar_movies['generos'].apply(lambda x: len(set(generos) & set(x)))
        top_recommendations = similar_movies.sort_values(by='shared_count', ascending=False).head(5)

        if top_recommendations.empty:
            return [] 

        # Return a list of recommended movies with their genres for flask
        return [f'{row["pelicula"]} (Genres: {row["generos"]})' for index, row in top_recommendations.iterrows()]
