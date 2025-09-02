import pandas as pd
import re # Regex
import html

from coleta_dados import coleta_dados   

noticias_brutas = coleta_dados()

if not noticias_brutas:
    print("Nenhuma notícia coletada.")
else:
    print(f"{len(noticias_brutas)} notícias.")
    df = pd.DataFrame(noticias_brutas)

    def sem_html(texto):
        texto = html.unescape(texto)
        return re.sub(r'<.*?>', '', texto)
    
    df['descricao'] = df['descricao'].apply(sem_html)
    df['titulo'] = df['titulo'].apply(sem_html)

    print(df[['titulo', 'descricao']])