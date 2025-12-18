import streamlit as st
import pandas as pd

from cerinte.cerinta1 import cerinta1
from cerinte.cerinta2 import cerinta2
from cerinte.cerinta3 import cerinta3
from cerinte.cerinta4 import cerinta4
from cerinte.cerinta5 import cerinta5

st.set_page_config(
    page_title="EDA cu Streamlit",
    layout="wide"
)

st.title("📊 Exploratory Data Analysis (EDA)")
st.write("Aplicatie Streamlit pentru analiza exploratorie a datelor.")

# =========================
# Incarcare date (pagina)
# =========================
st.header("📂 Incarcare date")

uploaded_file = st.file_uploader(
    "Incarca fisier CSV sau Excel",
    type=["csv", "xlsx"]
)

df = None

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("Fisier incarcat cu succes")

    except Exception as e:
        st.error(f"Eroare la citirea fisierului: {e}")

# =========================
# SIDEBAR – Navigare
# =========================
st.sidebar.header("📌 Navigare")

page = st.sidebar.radio(
    "Selecteaza cerinta",
    [
        "Prezentare",
        "Cerinta 1",
        "Cerinta 2",
        "Cerinta 3",
        "Cerinta 4",
        "Cerinta 5"
    ]
)

# =========================
# CONTINUT PRINCIPAL
# =========================
if df is None:
    st.info("Incarca un fisier pentru a incepe analiza.")
else:
    st.success(f"Dataset incarcat: {df.shape[0]} randuri × {df.shape[1]} coloane")

    if page == "Prezentare":
        st.header("📌 Prezentare dataset")
        st.write("Primele 10 randuri din dataset:")
        st.dataframe(df.head(10))

    elif page == "Cerinta 1":
        cerinta1(df)

    elif page == "Cerinta 2":
        cerinta2(df)

    elif page == "Cerinta 3":
        cerinta3(df)

    elif page == "Cerinta 4":
        cerinta4(df)

    elif page == "Cerinta 5":
        cerinta5(df)
