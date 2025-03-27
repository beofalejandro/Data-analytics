import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

try:
    data = pd.read_csv('C:/Users/HP/Documents/GitHub/Data-analytics/mobile_app_user_dataset_1.xlsx', delimiter=",")
except(pd.errors.ParserError):
   print("Error: No se pudo abrir el archivo. Por favor, verifique que el archivo existe y que tenga el formato correcto.")
   data = pd.read_csv('C:/Users/HP/Documents/GitHub/Data-analytics/mobile_app_user_dataset_1.xlsx', engine="openpyxl")

def mostrar_distribucion(data):
    """Para mostrar la distribución de datos"""
    # Iterar sobre cada columna del DataFrame
    for column in data.columns:
        plt.figure(figsize=(10, 6))

        # Comprobar si la columna es numérica
        if pd.api.types.is_numeric_dtype(data[column]):
            # Histograma para variables numéricas
            sns.histplot(data[column], bins=20, kde=True, color="blue", alpha=0.7)
            plt.title(f'Distribución de {column}')
            plt.ylabel("Frecuencia")
        else:
            # Gráfico de barras para variables categóricas
            sns.countplot(data=data, x=column, palette="Set2", alpha=0.7)
            plt.title(f'Distribución de {column}')
            plt.ylabel("Frecuencia")
            plt.xlabel(column)

        plt.grid(axis='y', alpha=0.75)
        plt.tight_layout()  # Mejora la presentación
        plt.show()

# Llamar a la función
mostrar_distribucion(data)