import streamlit as st
import numpy as np
import plotly.express as px

def cerinta3(df):
    st.header("Cerinta 3 - Analiza coloana numerica")

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    if not numeric_cols:
        st.warning("Nu exista coloane numerice in dataset.")
        return

    col = st.selectbox("Selecteaza coloana numerica", numeric_cols)

    bins = st.slider("Numar de bins", 10, 100, 30)

    # Histogram
    fig_hist = px.histogram(
        df,
        x=col,
        nbins=bins,
        title=f"Histograma pentru {col}"
    )
    st.plotly_chart(fig_hist, use_container_width=True)

    # Box plot
    fig_box = px.box(
        df,
        y=col,
        title=f"Box plot pentru {col}"
    )
    st.plotly_chart(fig_box, use_container_width=True)

    # Statistici
    st.subheader("Statistici")
    st.write(f"Media: {df[col].mean()}")
    st.write(f"Mediana: {df[col].median()}")
    st.write(f"Deviația standard: {df[col].std()}")
