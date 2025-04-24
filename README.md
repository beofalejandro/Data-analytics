# README - Knowledge Engineering Projects

0.9 Stable

This repository contains projects related to Knowledge Engineering, developed as part of different topics. Below is a description of the projects included in each thematic folder:

## Topic 1: Data Analytics

This folder contains a data analytics project that uses a CSV file with information about cyberattacks. The goal of the project is to extract insights and display them in an interactive dashboard developed with **Streamlit**.

### Main Files

- `ciberataques.csv`: Dataset with information about cyberattacks.
- `dashboard.py`: Python script that generates the interactive dashboard using Streamlit.

### How to Run

1. Install the required dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the dashboard with:

    ```bash
    streamlit run dashboard.py
    ```

---

## Topic 2: Movie Recommendation System

This project uses **Prolog** to implement a rule-based movie recommendation system. The system recommends movies based on user preferences.

### Main Files

- `recomendador.pl`: Prolog file containing the rules and knowledge base for recommendations.

### How to Run

1. Open the `recomendador.pl` file in a Prolog interpreter.
2. Make queries to get recommendations, for example:

    ```prolog
    ?- recomendar_pelicula(action, Recommendation).
    ```

---

## Topic 3: Family Tree

This folder contains a project that implements a family tree using **Prolog** and the **PySWIP** library to integrate it with Python. The system allows queries about family relationships.

### Main Files

- `arbol_genealogico.pl`: Prolog file with the knowledge base of the family tree.
- `consultas.py`: Python script that uses PySWIP to query the family tree.

### How to Run

1. Install PySWIP by running:

    ```bash
    pip install pyswip
    ```

2. Run the query script with:

    ```bash
    python consultas.py
    ```

## Requirements

- Python 3.8 or higher
- Prolog (SWI-Prolog recommended)
- Additional libraries specified in the `requirements.txt` files of each project.

---

Made with ❤️ for Alejandro Barrientos Escalante and ESCALIA Corporation
