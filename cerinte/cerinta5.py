import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd

def cerinta5(df):
    st.header("Cerinta 5 - Corelatii si outlieri")

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    if len(numeric_cols) < 2:
        st.warning("Nu exista suficiente coloane numerice pentru analiza.")
        return

    # =========================
    # Matrice de corelatie
    # =========================
    corr = df[numeric_cols].corr()

    fig_corr = px.imshow(
        corr,
        text_auto=True,
        title="Matrice de corelatie"
    )
    st.plotly_chart(fig_corr, use_container_width=True)

    # =========================
    # Scatter plot + Pearson
    # =========================
    x = st.selectbox("Variabila X", numeric_cols)
    y = st.selectbox("Variabila Y", numeric_cols, index=1)

    fig_scatter = px.scatter(
        df,
        x=x,
        y=y,
        title=f"Scatter plot: {x} vs {y}"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    pearson = df[x].corr(df[y])
    st.write(f"Coeficient de corelatie Pearson: {pearson}")

    # =========================
    # Outlieri - metoda IQR
    # =========================
    st.subheader("Detectie outlieri (IQR)")

    outlier_summary = []

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        outliers = df[
            (df[col] < Q1 - 1.5 * IQR) |
            (df[col] > Q3 + 1.5 * IQR)
        ]

        outlier_summary.append({
            "Coloana": col,
            "Numar outlieri": len(outliers),
            "Procent (%)": (len(outliers) / len(df)) * 100
        })

        # Vizualizare outlieri
        fig_box = px.box(
            df,
            y=col,
            title=f"Outlieri pentru {col}"
        )
        st.plotly_chart(fig_box, use_container_width=True)

    summary_df = pd.DataFrame(outlier_summary)
    st.subheader("Rezumat outlieri")
    st.dataframe(summary_df)
