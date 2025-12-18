import streamlit as st
import plotly.express as px

def cerinta4(df):
    st.header("Cerinta 4 - Analiza coloana categorica")

    cat_cols = df.select_dtypes(include="object").columns.tolist()

    if not cat_cols:
        st.warning("Nu exista coloane categorice in dataset.")
        return

    col = st.selectbox("Selecteaza coloana categorica", cat_cols)

    freq = df[col].value_counts()
    freq_df = freq.reset_index()
    freq_df.columns = [col, "Frecventa"]
    freq_df["Procent (%)"] = freq_df["Frecventa"] / len(df) * 100

    # Bar chart
    fig = px.bar(
        freq_df,
        x=col,
        y="Frecventa",
        title=f"Distributia valorilor pentru {col}"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Tabel frecvente
    st.dataframe(freq_df)
