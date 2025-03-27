import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.title("Análisis de Datos con Streamlit")

uploaded_file = st.file_uploader("Sube un archivo XLSX o CSV", type=["xlsx", "csv"])
if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Asegurarse de que la columna 'Timestamp' esté en formato de fecha
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

    st.title("Reporte de Ataques Cibernéticos")

    # Selección de columna para análisis adicional
    column = st.selectbox("Selecciona una columna para análisis adicional", df.columns)

    # 1. Histograma de la columna seleccionada
    st.write(f"Histograma de la columna '{column}':")
    plt.figure(figsize=(8, 4))
    sns.histplot(df[column], bins=30, kde=True, color='blue', alpha=0.7)
    plt.title(f'Histograma de {column}')
    plt.xlabel(column)
    plt.ylabel('Frecuencia')
    st.pyplot(plt)

    # 2. Selección de Tipo de Ataque para Filtrar
    attack_type_filter = st.selectbox("Selecciona el Tipo de Ataque", df['Attack Type'].unique())

    # Filtrar el DataFrame según el tipo de ataque seleccionado
    filtered_df = df[df['Attack Type'] == attack_type_filter]

    # 3. KPI: Número Total de Incidentes Filtrados
    total_incidents = filtered_df.shape[0]
    st.write(f"Número Total de Incidentes para el tipo de ataque '{attack_type_filter}': {total_incidents}")

    # 4. Gráfico de Aguja (Gauge para Total de Incidentes Filtrados)
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=total_incidents,
        title={'text': f"Total de Incidentes: {attack_type_filter}"},
        gauge={'axis': {'range': [0, max(100, total_incidents + 50)]},
               'bar': {'color': "blue"},
               'steps': [{'range': [0, total_incidents], 'color': "lightblue"},
                         {'range': [total_incidents, 100], 'color': "lightgray"}],
              }
    ))
    st.plotly_chart(fig)

    if 'Attack Type' in df.columns and 'Severity Level' in df.columns:
        st.write("Distribución de Severidad de Incidentes por Tipo de Ataque (Gráfico de Barras Apiladas):")

        severity_counts = filtered_df.groupby(['Attack Type', 'Severity Level']).size().unstack(fill_value=0)

        ax = severity_counts.plot(kind='bar', stacked=True, figsize=(10, 6))
        plt.title('Distribución de Severidad de Incidentes por Tipo de Ataque')
        plt.xlabel('Tipo de Ataque')
        plt.ylabel('Número de Incidentes')
        plt.xticks(rotation=45)

        st.pyplot(plt)

    if 'Protocol' in df.columns:
        st.write("Distribución de Incidentes por Protocolo (Gráfico de Pastel):")

        protocol_counts = filtered_df['Protocol'].value_counts()

        plt.figure(figsize=(10, 6))
        plt.pie(protocol_counts, labels=protocol_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title('Distribución de Incidentes por Protocolo')
        st.pyplot(plt)

    st.write("### Gráfica de Dispersión")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Timestamp', y='Severity Level', hue='Attack Type', style='Protocol')
    plt.title('Gráfica de Dispersión: Severity Level vs. Timestamp')
    plt.xlabel('Timestamp')
    plt.ylabel('Severity Level')
    st.pyplot(plt)

    st.write("### Histogramas")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Severity Level'], bins=5, kde=True, color='blue', alpha=0.7)
    plt.title('Histograma de Severity Level')
    plt.xlabel('Severity Level')
    plt.ylabel('Frecuencia')
    st.pyplot(plt)

    st.write("### Gráfico de Pareto")
    pareto_data = df['Attack Type'].value_counts()
    fig = plt.figure(figsize=(10, 6))
    plt.bar(pareto_data.index, pareto_data.values, color='skyblue')
    plt.title('Gráfico de Pareto: Tipos de Ataques')
    plt.xlabel('Tipos de Ataques')
    plt.ylabel('Número de Incidentes')
    plt.xticks(rotation=45)


    cum_percentage = pareto_data.cumsum() / pareto_data.sum() * 100
    plt.twinx()  # Crear un segundo eje y
    plt.plot(pareto_data.index, cum_percentage, color='red', marker='o', label='Porcentaje Acumulado')
    plt.ylabel('Porcentaje Acumulado (%)')
    plt.axhline(80, color='gray', linestyle='--')
    plt.legend(loc='upper left')
    st.pyplot(fig)

    st.title("Reporte de Ataques Cibernéticos")

    # Mapa de Árbol: Niveles de Severidad por Tipo de Ataque
    if 'Severity Level' in df.columns and 'Attack Type' in df.columns:
        st.write("### Mapa de Árbol: Niveles de Severidad por Tipo de Ataque")
        
        # Agrupación de datos para el treemap
        treemap_data_attack = df.groupby(['Attack Type', 'Severity Level']).size().reset_index(name='Incident Count')
        treemap_attack = px.treemap(treemap_data_attack, path=['Attack Type', 'Severity Level'], 
                                     values='Incident Count',
                                     color='Incident Count', 
                                     color_continuous_scale='RdBu')
        st.plotly_chart(treemap_attack)

    # Mapa de Árbol: Niveles de Severidad por Protocolo
    if 'Severity Level' in df.columns and 'Protocol' in df.columns:
        st.write("### Mapa de Árbol: Niveles de Severidad por Protocolo")
        
        # Agrupación de datos para el treemap
        treemap_data_protocol = df.groupby(['Protocol', 'Severity Level']).size().reset_index(name='Incident Count')
        treemap_protocol = px.treemap(treemap_data_protocol, path=['Protocol', 'Severity Level'], 
                                       values='Incident Count', 
                                       title='Mapa de Árbol: Severidad por Protocolo', 
                                       color='Incident Count', 
                                       color_continuous_scale='RdBu')
        st.plotly_chart(treemap_protocol)

else:
    st.write("Por favor, sube un archivo para comenzar el análisis.")