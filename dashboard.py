import streamlit as st
import pandas as pd
from processamento_dados import processar_dados

st.set_page_config( layout="wide")

st.title("📊 Painel de Monitoramento de Notícias sobre IA no Piauí")
st.markdown("---")

@st.cache_data 
def carregar_dados():
    df = processar_dados()
    return df

with st.spinner('Coletando e processando as notícias mais recentes...'):
    df_noticias = carregar_dados()

if df_noticias.empty:
    st.warning("Nenhuma notícia encontrada ou falha na coleta.")
else:
    st.write(df_noticias[['titulo', 'descricao', 'sentimento']])

    st.header("Detalhes das Noticias Coletadas")

    st.dataframe(df_noticias[['titulo', 'sentimento', 'link']].reset_index())