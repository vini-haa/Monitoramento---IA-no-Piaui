import requests # Faz requisições HTTP
import urllib.parse # Manipula URLs
import xml.etree.ElementTree as ET # Processa XML

query = "Inteligência Artificial Piauí"
query_formatada = urllib.parse.quote(query) # Formata a query para URL

url = f"https://news.google.com/rss/search?q={query_formatada}&hl=pt-BR&gl=BR&ceid=BR:pt-42"
response = requests.get(url)

print(url)
print(f"Status Code: {response.status_code}")

arvore = ET.fromstring(response.content)
noticias =[]

for item in arvore.findall('.//item'):
    titulo = item.find('title').text
    link = item.find('link').text
    descricao = item.find('description').text

    noticias.append({
        'titulo': titulo,
        'link': link,
        'descricao': descricao
    })

print(len(noticias))
