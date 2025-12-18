import streamlit as st
import numpy as np

def cerinta1(df):
    st.header("Cerinta 1 - Incarcare si filtrare date")

    # Afisare primele 10 randuri
    st.subheader("Primele 10 randuri din dataset")
    st.dataframe(df.head(10))

    st.write(f"Numar randuri initial: {len(df)}")

    filtered_df = df.copy()

    # Identificare coloane
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    categorical_cols = df.select_dtypes(include="object").columns.tolist()

    # Filtrare numerica
    if numeric_cols:
        st.subheader("Filtrare coloane numerice")
        for col in numeric_cols:
            min_val = float(df[col].min())
            max_val = float(df[col].max())

            selected_range = st.slider(
                f"{col}",
                min_val,
                max_val,
                (min_val, max_val)
            )

            filtered_df = filtered_df[
                (filtered_df[col] >= selected_range[0]) &
                (filtered_df[col] <= selected_range[1])
            ]

    # Filtrare categorica
    if categorical_cols:
        st.subheader("Filtrare coloane categorice")
        for col in categorical_cols:
            selected_values = st.multiselect(
                f"{col}",
                options=df[col].dropna().unique(),
                default=df[col].dropna().unique()
            )

            filtered_df = filtered_df[filtered_df[col].isin(selected_values)]

    # Rezultate filtrare
    st.subheader("Rezultat filtrare")
    st.write(f"Numar randuri dupa filtrare: {len(filtered_df)}")
    st.dataframe(filtered_df)
