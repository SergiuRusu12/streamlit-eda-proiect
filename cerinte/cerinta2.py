import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def cerinta2(df):
    st.header("Cerinta 2 - Informatii generale despre dataset")

    # =========================
    # Dimensiune dataset
    # =========================
    st.subheader("Dimensiune dataset")
    st.write(f"Numar randuri: {df.shape[0]}")
    st.write(f"Numar coloane: {df.shape[1]}")

    # =========================
    # Tipuri de date
    # =========================
    st.subheader("Tipuri de date pentru fiecare coloana")
    dtype_df = pd.DataFrame({
        "Coloana": df.columns,
        "Tip de date": df.dtypes.astype(str)
    })
    st.dataframe(dtype_df)

    # =========================
    # Valori lipsa
    # =========================
    st.subheader("Valori lipsa")

    missing_count = df.isnull().sum()
    missing_pct = (missing_count / len(df)) * 100

    missing_df = pd.DataFrame({
        "Coloana": missing_count.index,
        "Valori lipsa": missing_count.values,
        "Procent (%)": missing_pct.values
    })

    missing_df = missing_df[missing_df["Valori lipsa"] > 0]

    if missing_df.empty:
        st.success("Nu exista valori lipsa in dataset.")
    else:
        st.dataframe(missing_df)

        # Grafic valori lipsa
        fig = px.bar(
            missing_df,
            y="Coloana",
            x="Procent (%)",
            orientation="h",
            title="Procent valori lipsa pe coloana"
        )
        st.plotly_chart(fig, use_container_width=True)

    # =========================
    # Statistici descriptive
    # =========================
    st.subheader("Statistici descriptive pentru coloane numerice")

    numeric_cols = df.select_dtypes(include=np.number)

    if numeric_cols.empty:
        st.warning("Nu exista coloane numerice in dataset.")
    else:
        stats_df = numeric_cols.describe().T
        st.dataframe(stats_df)
