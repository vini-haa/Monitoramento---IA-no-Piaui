import requests # Faz requisições HTTP
import urllib.parse # Manipula URLs
import xml.etree.ElementTree as ET # Processa XML

def coleta_dados(query = "Inteligência Artificial Piauí"):
    
    query_formatada = urllib.parse.quote(query) # Formata a query para URL

    url = f"https://news.google.com/rss/search?q={query_formatada}&hl=pt-BR&gl=BR&ceid=BR:pt-42"
    response = requests.get(url)

    arvore = ET.fromstring(response.content)
    noticias = []

    for item in arvore.findall('.//item'):
        if len(noticias) >= 15: # limito a 15 notícias
            break

        titulo = item.find('title').text
        link = item.find('link').text
        descricao = item.find('description').text

        noticias.append({
            'titulo': titulo,
            'link': link,
            'descricao': descricao
        })


    return noticias

if __name__ == '__main__':
    noticias_coletadas = coleta_dados()
    
    print(f"{len(noticias_coletadas)} notícias.")

    if noticias_coletadas:
        print("\n--- primeira notícia ---")
        print(noticias_coletadas[0])
