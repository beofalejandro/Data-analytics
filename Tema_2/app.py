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

    # Apply Apriori algorithm to find frequent itemsets and association rules
    frequent_itemsets = apriori(onehot_df, min_support=0.05, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.05) 

    # Function to recommend movies based on the viewed movie
    def recomendar(pelicula_vista):
        if pelicula_vista not in df['pelicula'].values:
            print(f'The movie "{pelicula_vista}" was not found in the database.')
            return
        
        generos = df.loc[df['pelicula'] == pelicula_vista, 'generos'].values[0]
        recomendaciones = rules[rules['antecedents'].apply(lambda x: any(item in generos for item in x))]

        print(f'Recommendations based on "{pelicula_vista}":')
        if recomendaciones.empty:
            print("No recommendations found.")
        else:
            for index, row in recomendaciones.iterrows():
                for genre in row['consequents']:
                    print(f'- {genre}')

    # TODO: Replace with the movie you have seen
    # Improve to genre recomendation
    # or movie recommendation based on the genre of the movie you have seen
    # Get asociated movies
    # Improve frontend to proyect
    pelicula_vista = 'Modern Times'
    recomendar(pelicula_vista)