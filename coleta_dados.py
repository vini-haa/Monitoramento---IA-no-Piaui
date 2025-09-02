import requests

url = "https://news.google.com/rss/search?q=Inteligência+Artificial+Piauí&hl=pt-BR&gl=BR&ceid=BR:pt-42"

response = requests.get(url)

print(f"Status Code: {response.status_code}")
