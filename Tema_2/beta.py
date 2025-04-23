import pandas as pd
import subprocess
import ast
from mlxtend.frequent_patterns import apriori, association_rules

# Get movies from Prolog file
# Will be in the same directory as the script "movies.pl"
def obtener_peliculas():
    process = subprocess.run(
        ['swipl', '-s', 'movies.pl', '-g', 'findall(Name-Genres, pelicula(Name, Genres), L), write(L), halt.', '-t', 'halt'], 
        capture_output=True, text=True
    )
    
    # Get the results from the Prolog query
    result = process.stdout.strip()
    peliculas_data = []
    

    for item in result[1:-1].split(','):
        item = item.strip()
        if '-' in item: # Check if the item contains a dash
            name, genres = item.split('-')
            name = name.strip().strip("'")
            genres = ast.literal_eval(genres.strip())
            peliculas_data.append((name, genres))
    
    return peliculas_data

# Get movies data
data = obtener_peliculas()

# Check if data is empty
if not data:
    print("No se encontraron películas.")
else:
    # Create a datarame from the data
    df = pd.DataFrame(data, columns=['pelicula', 'generos'])

    # Apply apriori algorithm to find frequent itemsets and association rules
    def create_transaction_list(df):
        return df['generos'].tolist()

    # Crear lista de transacciones
    transaction_list = create_transaction_list(df)

    # Create one-hot encoded DataFrame
    from mlxtend.preprocessing import TransactionEncoder
    encoder = TransactionEncoder()
    encoded_array = encoder.fit(transaction_list).transform(transaction_list)
    onehot_df = pd.DataFrame(encoded_array, columns=encoder.columns_)

    # Get frequent itemsets
    frequent_itemsets = apriori(onehot_df, min_support=0.1, use_colnames=True)

    # Generate association rules
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)

    # Recomendation fuction
    def recomendar(pelicula_vista):
        generos = df.loc[df['pelicula'] == pelicula_vista, 'generos'].values[0]
        recomendaciones = rules[rules['antecedents'].apply(lambda x: any(item in generos for item in x))]

        print(f'Recomendaciones basadas en "{pelicula_vista}":')
        for index, row in recomendaciones.iterrows():
            for genre in row['consequents']:
                print(f'- {genre}')

    # Example usage
    pelicula_vista = 'Interstellar'
    recomendar(pelicula_vista)