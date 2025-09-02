import streamlit as st
import pandas as pd
from processamento_dados import processar_dados
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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
    total_noticias = len(df_noticias)
    sent_positivos = len(df_noticias[df_noticias['sentimento'] == 'Positivo'])
    sent_negativos = len(df_noticias[df_noticias['sentimento'] == 'Negativo'])
    sent_neutros = len(df_noticias[df_noticias['sentimento'] == 'Neutro']) 
    
   
    col_metrics1, col_metrics2, col_metrics3, col_metrics4 = st.columns(4)
    col_metrics1.metric("Total de Notícias", f"{total_noticias} ")
    col_metrics2.metric("Notícias Positivas", f"{sent_positivos} ")
    col_metrics3.metric("Notícias Neutras", f"{sent_neutros} ")
    col_metrics4.metric("Notícias Negativas", f"{sent_negativos} ")
    st.markdown("---") 

    st.header("Detalhes das Notícias Coletadas")
    st.dataframe(df_noticias[['titulo', 'sentimento', 'link']])
    st.markdown("---")

    
    col_grafico1, col_grafico2 = st.columns(2)

    with col_grafico1:
        st.header("Distribuição de Sentimentos")
        sentiment_counts = df_noticias['sentimento'].value_counts()
        
        import plotly.express as px
        fig_pie = px.pie(sentiment_counts, 
                         values=sentiment_counts.values, 
                         names=sentiment_counts.index,
                         title='Distribuição dos Sentimentos',
                         color=sentiment_counts.index,
                         color_discrete_map={'Positivo':'green', 'Negativo':'red', 'Neutro':'royalblue'})
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_grafico2:
        st.header("Termos Mais Frequentes")
        texto_completo = " ".join(df_noticias['texto_completo'])
    
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto_completo)
        
        fig_wc, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig_wc)

        st.markdown("---")
        with st.expander("⚠️ Clique aqui para saber mais sobre as limitações do modelo"):
            st.write("""Esta análise de sentimento é baseada em regras simples e pode não capturar sarcasmo ou contextos complexos
    """)